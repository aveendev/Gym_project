from rest_framework import serializers
from .models import Schedule, Equipment
from gym_core.models import Player, Coach
from memberships.models import Subscription

class ScheduleSerializer(serializers.ModelSerializer):
    training_category = serializers.SerializerMethodField()
    player_name = serializers.ReadOnlyField(source='player.full_name')
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
            'player', 
            'player_name', 
            'coach', 
            'coach_name', 
            'player_attendance',
            'coach_attendance',
            'training_category'
        ]

    def get_training_category(self, obj):
       if obj.player:
          return obj.player.get_training_type_display()
       else:
          return "غير محدد"

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['id', 'name', 'quantity', 'price', 'last_updated']