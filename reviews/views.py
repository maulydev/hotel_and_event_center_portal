from rest_framework import viewsets
from .models import Review
from .serializers import ReviewSerializer, ReviewCreateSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    
    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return ReviewCreateSerializer
        return ReviewSerializer