

from rest_framework import serializers
from .models import Coach,Player

class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    coach_name = serializers.ReadOnlyField(source = 'coach.full_name')
    class Meta:
        model = Player
        fields =[ 'full_name',
            'father_name',
            'mother_name',
            'birth_date',
            'phone_number',
            'sport_type',
            'training_type',
            'weight',
            'coach_name']