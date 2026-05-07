from rest_framework import serializers
from .models import Subscription
from gym_core.models import Player

class SubscriptionSerializer(serializers.ModelSerializer):
    player_name = serializers.ReadOnlyField(source='player.full_name')
    training_display = serializers.ReadOnlyField(source='player.get_training_type_display')

    class Meta:
        model = Subscription
        fields = [
            'id', 
            'player', 
            'player_name', 
            'training_display', 
            'start_date', 
            'end_date', 
            'price', 
            'is_paid'
        ]