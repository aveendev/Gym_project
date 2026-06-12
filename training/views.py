from django.shortcuts import render
from rest_framework import generics, permissions, filters  
from .models import Schedule, Equipment
from .serializers import ScheduleSerializer, EquipmentSerializer
from .filters import EquipmentFilter

class ScheduleListCreateView(generics.ListCreateAPIView):
    serializer_class = ScheduleSerializer
    filterset_fields = ['day']
    search_fields = ['^gymnastics_coach__full_name', '^karate_coach__full_name']
    ordering_fields = ['day', 'start_time', 'gymnastics_coach__full_name', 'karate_coach__full_name']
    ordering = ['day']
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get_queryset(self):
        return Schedule.objects.filter(gym=self.request.user.gym).select_related(
            'gymnastics_coach', 'karate_coach').prefetch_related('gymnastics_players', 'karate_players')
    def perform_create(self, serializer):
        serializer.save(gym=self.request.user.gym)


class ScheduleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ScheduleSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get_queryset(self):
        return Schedule.objects.filter(gym=self.request.user.gym).select_related(
            'gymnastics_coach','karate_coach' ).prefetch_related('gymnastics_players', 'karate_players')

class EquipmentList(generics.ListCreateAPIView):
    serializer_class = EquipmentSerializer
    filterset_class = EquipmentFilter
    ordering_fields = ['name', 'quantity']
    ordering = ['quantity'] 
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get_queryset(self):
        return Equipment.objects.filter(gym=self.request.user.gym)
    
    def perform_create(self, serializer):
        serializer.save(gym=self.request.user.gym)


class EquipmentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EquipmentSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get_queryset(self):
        return Equipment.objects.filter(gym=self.request.user.gym)