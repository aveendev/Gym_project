from rest_framework import viewsets,filters
from .models import GymnasticsPlayer,KaratePlayer, GymnasticsCoach,KarateCoach
from .serializers import GymnasticsPlayerSerializer,KaratePlayerSerializer , GymnasticsCoachSerializer,KarateCoachSerializer
from rest_framework.permissions import IsAuthenticated


# viewset for coach
class GymnasticsCoachViewSet(viewsets.ModelViewSet):
    queryset = GymnasticsCoach.objects.all()
    serializer_class = GymnasticsCoachSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name']

class KarateCoachViewSet(viewsets.ModelViewSet):
    queryset = KarateCoach.objects.all()
    serializer_class = KarateCoachSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name']


# viewset for player
class GymnasticsPlayerViewSet(viewsets.ModelViewSet):
    queryset = GymnasticsPlayer.objects.all()
    serializer_class = GymnasticsPlayerSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name']

class KaratePlayerViewSet(viewsets.ModelViewSet):
    queryset = KaratePlayer.objects.all()
    serializer_class = KaratePlayer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name']

