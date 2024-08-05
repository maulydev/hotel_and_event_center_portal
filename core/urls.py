from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
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

router = routers.DefaultRouter()
router.register(r'hotels', HotelViewSet)
router.register(r'profiles', UserProfileViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'payments', PaymentViewSet)

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
   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
   path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
