from rest_framework import viewsets
from .serializers import WorkhoursSerializers, EventCenterWorkhoursSerializers
from .models import Workhours, EventCenterWorkhours


class WorkhoursViewSet(viewsets.ModelViewSet):
    queryset = Workhours.objects.all()
    serializer_class = WorkhoursSerializers
    filterset_fields = ['hotel__hotel_number']



class EventCenterWorkhoursViewSet(viewsets.ModelViewSet):
    queryset = EventCenterWorkhours.objects.all()
    serializer_class = EventCenterWorkhoursSerializers
    filterset_fields = ['event_center__event_center_number']