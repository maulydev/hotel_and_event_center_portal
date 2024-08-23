from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from random_otp.generator import generate_numeric_otp
from datetime import timedelta
from django.utils import timezone
from .models import User, OtpHistory
from userprofile.models import UserProfile
from lib.otp import send_otp_sms
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='Phone number of the user'),
        },
        required=['phone_number'],
    ),
    responses={
        200: openapi.Response(
            description='OTP generated and sent successfully',
            examples={
                'application/json': {
                    'code': '200',
                    'message': 'OTP sent successfully'
                }
            }
        ),
        400: openapi.Response(
            description='Bad request',
            examples={
                'application/json': {
                    'error': 'Phone number not provided'
                }
            }
        ),
        404: openapi.Response(
            description='User not found',
            examples={
                'application/json': {
                    'error': 'User not found'
                }
            }
        ),
    }
)
@api_view(['POST'])
def generate_otp(request):
    phone_number = request.data.get('phone_number')
    
    if not phone_number:
        return Response({'error': 'Phone number not provided'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.filter(profile__phone_number=phone_number).first()
    
    if user:
        # Generate a 6-digit numeric OTP
        otp = generate_numeric_otp(6)
        
        # Create or update OTP history
        otp_history, created = OtpHistory.objects.update_or_create(
            phone_number=phone_number,
            defaults={
                'otp': otp,
                'expires_at': timezone.now() + timedelta(minutes=10)
            }
        )
        
        # Optionally send OTP via SMS here using Arkesel SMS API
        response = send_otp_sms(phone_number, otp)
        return Response({'code': response['code'], 'message': response['message']}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='Phone number of the user'),
            'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username for the account', nullable=True),
            'otp': openapi.Schema(type=openapi.TYPE_STRING, description='OTP for verification', nullable=True),
        },
        required=['phone_number'],  # Specify that phone_number is required
    ),
    responses={
        201: openapi.Response('User registered successfully'),
        400: openapi.Response('Bad request'),
        404: openapi.Response('User not found'),
    }
)
@api_view(['POST'])
def register(request):
    phone_number = request.data.get('phone_number')
    username = request.data.get('username')
    otp = request.data.get('otp')
    default_password = "Password@Default"

    if not phone_number:
        return Response({'error': 'Phone number is required'}, status=status.HTTP_400_BAD_REQUEST)

    # Scenario 1: If only the phone number is provided, generate and send OTP
    if phone_number and not username and not otp:
        user_exists = User.objects.filter(profile__phone_number=phone_number).exists()

        if user_exists:
            return Response({'error': 'User with this phone number already exists'}, status=status.HTTP_400_BAD_REQUEST)

        # Generate OTP
        generated_otp = generate_numeric_otp(6)

        # Save OTP history
        OtpHistory.objects.create(
            phone_number=phone_number,
            otp=generated_otp,
            expires_at=timezone.now() + timedelta(minutes=10)
        )
        
        # Optionally send OTP via SMS here
        response = send_otp_sms(phone_number, generated_otp)
        return Response({'code': response['code'], 'message': response['message']}, status=status.HTTP_200_OK)

    # Scenario 2: If phone number, username, and OTP are provided, register the user
    if phone_number and username and otp:
        # Verify if the OTP is correct
        otp_history = OtpHistory.objects.filter(phone_number=phone_number, otp=otp).first()

        if not otp_history or timezone.now() > otp_history.expires_at:
            return Response({'error': 'Invalid or expired OTP'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the user already exists
        if User.objects.filter(profile__phone_number=phone_number).exists():
            return Response({'error': 'User with this phone number already exists'}, status=status.HTTP_400_BAD_REQUEST)

        # Create the user
        user = User.objects.create_user(username=username, password=default_password)
        
        # Create the UserProfile instance
        profile = UserProfile.objects.create(user=user, phone_number=phone_number)

        # Optionally delete the used OTP history
        otp_history.delete()

        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

    return Response({'error': 'Incomplete data. Please provide the phone number, username, and OTP to register, or just the phone number to generate an OTP.'}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='Phone number of the user'),
            'otp': openapi.Schema(type=openapi.TYPE_STRING, description='One-time password (OTP) sent to the user'),
        },
        required=['phone_number', 'otp'],
    ),
    responses={
        200: openapi.Response(
            description='OTP verified successfully',
            examples={
                'application/json': {
                    'refresh': 'your_refresh_token_here',
                    'access': 'your_access_token_here',
                }
            }
        ),
        400: openapi.Response(
            description='Bad request',
            examples={
                'application/json': {
                    'error': 'Phone number and OTP must be provided'
                }
            }
        ),
        404: openapi.Response(
            description='User not found',
            examples={
                'application/json': {
                    'error': 'User not found'
                }
            }
        ),
    }
)
@api_view(['POST'])
def verify_otp(request):
    phone_number = request.data.get('phone_number')
    otp = request.data.get('otp')

    if not phone_number or not otp:
        return Response({'error': 'Phone number and OTP must be provided'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.filter(profile__phone_number=phone_number).first()

    if not user:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    otp_history = OtpHistory.objects.filter(phone_number=phone_number, otp=otp).first()

    if not otp_history:
        return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)

    if timezone.now() > otp_history.expires_at:
        return Response({'error': 'OTP has expired'}, status=status.HTTP_400_BAD_REQUEST)

    # Mark the user as verified (optional)
    user.is_active = True
    user.save()

    # Optionally, generate a JWT token for the user
    # refresh = RefreshToken.for_user(user)
    # return Response({
    #     'refresh': str(refresh),
    #     'access': str(refresh.access_token),
    # }, status=status.HTTP_200_OK)
    profile_picture_url = None
    if user.profile.profile_picture and user.profile.profile_picture.name:
        profile_picture_url = user.profile.profile_picture.url

    return Response({
        'user_id': user.id,
        'username': user.username,
        'phone_number': user.profile.phone_number,
        'role': user.profile.role,
        'profile_picture': profile_picture_url
    }, status=status.HTTP_200_OK)