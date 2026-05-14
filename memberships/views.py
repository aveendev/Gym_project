from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Subscription
from .serializers import SubscriptionSerializer

class SubscriptionListCreateView(generics.ListCreateAPIView):
    queryset = Subscription.objects.select_related('player').all()
    serializer_class = SubscriptionSerializer
    filterset_fields = ['is_paid', 'player__full_name'] 
    search_fields = ['^player__full_name']
    ordering_fields = ['is_paid', 'start_date', 'price']
    ordering = ['is_paid'] 

    def get_permissions(self):
        if self.request.method == 'POST':    
            return [permissions.IsAuthenticated(), permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]


class SubscriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.select_related('player').all()
    serializer_class = SubscriptionSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated(), permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]
