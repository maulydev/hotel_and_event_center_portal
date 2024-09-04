from rest_framework import viewsets
from .models import Facilities, EventCenterFacilities
from .serializers import FacilitiesSerializers, EventCenterFacilitiesSerializer


class FacilitiesViewSet(viewsets.ModelViewSet):
    queryset = Facilities.objects.all()
    serializer_class = FacilitiesSerializers
    filterset_fields = ['hotel']
    
    
    
class EventCenterFacilitiesViewSet(viewsets.ModelViewSet):
    queryset = EventCenterFacilities.objects.all()
    serializer_class = EventCenterFacilitiesSerializer
    filterset_fields = ['event_center']