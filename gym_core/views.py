from rest_framework import viewsets,filters
from .models import GymnasticsPlayer,KaratePlayer, GymnasticsCoach,KarateCoach
from .serializers import KaratePlayerSerializer , GymnasticsCoachSerializer,KarateCoachSerializer,GymnasticsPlayerSerializer
from rest_framework import  permissions


# viewset for coach
class GymnasticsCoachViewSet(viewsets.ModelViewSet):
    serializer_class = GymnasticsCoachSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name']

    def get_queryset(self):
        return GymnasticsCoach.objects.filter(gym=self.request.user.gym)
    
    def perform_create(self, serializer):
        serializer.save(gym=self.request.user.gym)
    
class KarateCoachViewSet(viewsets.ModelViewSet):
    serializer_class = KarateCoachSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name']
    def get_queryset(self):
        return KarateCoach.objects.filter(gym=self.request.user.gym)
    
    def perform_create(self, serializer):
        serializer.save(gym=self.request.user.gym)


# viewset for player
class GymnasticsPlayerViewSet(viewsets.ModelViewSet):
    serializer_class = GymnasticsPlayerSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name']

    def get_queryset(self):
        return GymnasticsPlayer.objects.filter(gym=self.request.user.gym)
    
    def perform_create(self, serializer):
        serializer.save(gym=self.request.user.gym)

class KaratePlayerViewSet(viewsets.ModelViewSet):
    serializer_class = KaratePlayerSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name']

    def get_queryset(self):
        return KaratePlayer.objects.filter(gym=self.request.user.gym)
    
    def perform_create(self, serializer):
        serializer.save(gym=self.request.user.gym)

