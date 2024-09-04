from rest_framework import viewsets
from .models import Review, EventCenterReview
from .serializers import ReviewSerializer, ReviewCreateSerializer, EventCenterReviewSerializer, EventCenterReviewCreateSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    filterset_fields = ['hotel__hotel_number']
    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return ReviewCreateSerializer
        return ReviewSerializer
    
    
class EventCenterReviewViewSet(viewsets.ModelViewSet):
    queryset = EventCenterReview.objects.all()
    filterset_fields = ['event_center__event_center_number']
    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return EventCenterReviewCreateSerializer
        return EventCenterReviewSerializer