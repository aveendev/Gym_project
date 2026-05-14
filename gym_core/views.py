from rest_framework import viewsets,filters
from .models import Player, Coach
from .serializers import PlayerSerializer , CoachSerializer
from rest_framework.permissions import IsAuthenticated


# viewset for coach
class CoachViewSet(viewsets.ModelViewSet):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name']

# viewset for player
class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_name']

