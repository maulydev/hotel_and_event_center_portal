from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

from hotels.views import HotelViewSet
from userprofile.views import UserProfileViewSet
from reviews.views import ReviewViewSet
from rooms.views import RoomViewSet
from bookings.views import BookingViewSet
from payments.views import PaymentViewSet
from amenities.views import AmenityViewSet
from facilities.views import FacilitiesViewSet
from workhours.views import WorkhoursViewSet
from workhours.views import EventCenterWorkhoursViewSet
from gallery.views import GalleryViewset
from gallery.views import EventCenterGalleryViewset
from auth_user.views import generate_otp, verify_otp, register
from event_centers.views import EventCenterViewSet, EventBookingViewSet

router = routers.DefaultRouter()
router.register(r'hotels', HotelViewSet)
router.register(r'profiles', UserProfileViewSet)
router.register(r'reviews', ReviewViewSet, basename='reviews')
router.register(r'rooms', RoomViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'amenities', AmenityViewSet)
router.register(r'facilities', FacilitiesViewSet)
router.register(r'workhours', WorkhoursViewSet)
router.register(r'event-center-workhours', EventCenterWorkhoursViewSet)
router.register(r'gallery', GalleryViewset)
router.register(r'event-center-gallery', EventCenterGalleryViewset)
router.register(r'event-centers', EventCenterViewSet)
router.register(r'event-bookings', EventBookingViewSet)


# django admin site customization
admin.site.site_header = "Hotel Booking System"
admin.site.site_title = "Hotel Booking System"
admin.site.index_title = "Hotel Booking System"

schema_view = get_schema_view(
      openapi.Info(
         title="Hotel Booking System API",
         default_version='v1',
         description="Hotel Booking System API Documentation",
         terms_of_service="https://www.google.com/policies/terms/",
         contact=openapi.Contact(email="contact@snippets.local"),
         license=openapi.License(name="BSD License"),
      ),
      public=True,
      permission_classes=(permissions.AllowAny,),
   )

urlpatterns = [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('admin/', admin.site.urls),
   path('api/token/generate-otp/', generate_otp, name='generate_otp'),
   path('api/token/verify-otp/', verify_otp, name='verify_otp'),
   path('api/token/register/', register, name='register'),
   path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)