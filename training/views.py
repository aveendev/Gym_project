from django.shortcuts import render
from rest_framework import generics, permissions,filters  
from .models import Schedule, Equipment
from .serializers import ScheduleSerializer, EquipmentSerializer
from .filters import EquipmentFilter

class ScheduleListCreateView(generics.ListCreateAPIView):
    queryset = Schedule.objects.select_related('coach').prefetch_related('players').all()
    serializer_class = ScheduleSerializer
    filterset_fields = ['day']
    search_fields = ['^coach__full_name']
    ordering_fields = ['day', 'start_time', 'couch__full_name']
    ordering = ['day']
    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated(), permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]

class ScheduleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.select_related('coach').prefetch_related('players').all()
    serializer_class = ScheduleSerializer
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated(), permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]

class EquipmentList(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    filterset_class = EquipmentFilter
    ordering_fields = ['name', 'quantity']
    ordering = ['quantity'] 

    def get_permissions(self):
        if self.request.method == 'POST':
             return [permissions.IsAuthenticated(), permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]

class EquipmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
           return [permissions.IsAuthenticated(), permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]
