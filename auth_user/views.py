from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from random_otp.generator import generate_numeric_otp
from datetime import timedelta
from django.utils import timezone
import requests
from .models import User, OtpHistory


def send_otp_sms(phone_number, otp):
    # url = 'https://api.msg91.com/api/sendhttp.php'
    api_key = ''
    sender_id = 'ercodr(TM)'
    message = f'Your Verfication code is: {otp}'
    recipient = phone_number
    url = f'https://sms.arkesel.com/sms/api?action=send-sms&api_key={api_key}&to={recipient}&from={sender_id}&sms={message}'
    response = requests.get(url)
    return response
    

@api_view(['POST'])
def generate_otp(request):
    username = request.data.get('phone_number')
    
    if not username:
        return Response({'error': 'Phone number not provided'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.filter(username=username).first()
    
    if user:
        # Generate a 6-digit numeric OTP
        otp = generate_numeric_otp(6)
        
        # Create or update OTP history
        otp_history, created = OtpHistory.objects.update_or_create(
            user=user,
            defaults={
                'otp': otp,
                'expires_at': timezone.now() + timedelta(minutes=10)
            }
        )
        
        # Optionally send OTP via SMS here using Arkesel SMS API
        # send_otp_sms(username, otp)
        print("Verification code:", otp)
        return Response({'otp': otp}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def verify_otp(request):
    username = request.data.get('phone_number')
    otp = request.data.get('otp')
    
    if not username or not otp:
        return Response({'error': 'Phone number and OTP must be provided'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.filter(username=username).first()
    
    if not user:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
    otp_history = OtpHistory.objects.filter(user=user, otp=otp).first()
    
    if not otp_history:
        return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
    
    if otp_history.expires_at < timezone.now():
        return Response({'error': 'OTP expired'}, status=status.HTTP_400_BAD_REQUEST)
    
    # If OTP is valid and not expired, authenticate the user
    # Generate JWT tokens
    refresh = RefreshToken.for_user(user)
    
    # Optionally, you can delete the OTP history after successful verification
    otp_history.delete()
    
    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }, status=status.HTTP_200_OK)
