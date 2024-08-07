from rest_framework import viewsets
from .models import Facilities
from .serializers import FacilitiesSerializers


class FacilitiesViewSet(viewsets.ModelViewSet):
    queryset = Facilities.objects.all()
    serializer_class = FacilitiesSerializers
    filterset_fields = ['hotel']