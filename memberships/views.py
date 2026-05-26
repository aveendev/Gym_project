from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Subscription
from .serializers import SubscriptionSerializer

class SubscriptionListCreateView(generics.ListCreateAPIView):
    serializer_class = SubscriptionSerializer
    filterset_fields = ['is_paid', 'gymnastics_player__phone_number', 'karate_player__phone_number'] 
    search_fields = ['gymnastics_player__full_name','karate_player__full_name','karate_player__phone_number','gymnastics_player__phone_number']
    ordering_fields = ['is_paid', 'start_date', 'price']
    ordering = ['is_paid'] 
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get_queryset(self):
        return Subscription.objects.filter(gym=self.request.user.gym).select_related('gymnastics_player', 'karate_player')
    def perform_create(self, serializer):
        serializer.save(gym=self.request.user.gym)


class SubscriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get_queryset(self):
        return Subscription.objects.filter( gym=self.request.user.gym).select_related('gymnastics_player', 'karate_player')