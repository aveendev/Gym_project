from rest_framework import serializers
from .models import Schedule, Equipment
from gym_core.models import Coach,Player
from memberships.models import Subscription

class ScheduleSerializer(serializers.ModelSerializer):
    player_names = serializers.SlugRelatedField(source= 'players',many=True, read_only=True, slug_field='full_name')
    coach_name = serializers.ReadOnlyField(source='coach.full_name')
    day_display = serializers.ReadOnlyField(source='get_day_display')
    class Meta:
        model = Schedule
        fields = [
            'id', 
            'day', 
            'day_display',
            'start_time', 
            'end_time', 
            'players', 
            'player_names', 
            'coach', 
            'coach_name',
        ]

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['id', 'name', 'quantity', 'price', 'last_updated']
        