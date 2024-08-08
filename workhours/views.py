from rest_framework import viewsets
from .serializers import WorkhoursSerializers
from .models import Workhours


class WorkhoursViewSet(viewsets.ModelViewSet):
    queryset = Workhours.objects.all()
    serializer_class = WorkhoursSerializers
    filterset_fields = ['hotel__hotel_number']