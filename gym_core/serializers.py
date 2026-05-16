

from rest_framework import serializers
from .models import GymnasticsCoach,KarateCoach,GymnasticsPlayer,KaratePlayer

class GymnasticsCoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymnasticsCoach
        fields = '__all__'

class KarateCoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = KarateCoach
        fields = '__all__'



class GymnasticsPlayerSerializer(serializers.ModelSerializer):
    coach_name = serializers.ReadOnlyField(source = 'gymnastics_coach.full_name')
    class Meta:
        model = GymnasticsPlayer
        fields =[ 'full_name',
            'father_name',
            'mother_name',
            'birth_date',
            'phone_number',
            'training_type',
            'weight',
            'gymnastics_coach',
            'coach_name'
            ]
        
class KaratePlayerSerializer(serializers.ModelSerializer):
    coach_name = serializers.ReadOnlyField(source = 'karate_coach.full_name')
    class Meta:
        model = KaratePlayer
        fields =[ 'full_name',
            'father_name',
            'mother_name',
            'birth_date',
            'phone_number',
            'training_type',
            'weight',
            'karate_coach',
            'coach_name'
            ]