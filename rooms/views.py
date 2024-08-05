from rest_framework import viewsets
from .models import Room
from .serializers import RoomSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filterset_fields = ['hotel__hotel_number', 'is_available', 'room_type', 'price_per_night']