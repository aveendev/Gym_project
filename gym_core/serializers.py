

from rest_framework import serializers
from .models import GymnasticsCoach,KarateCoach,GymnasticsPlayer,KaratePlayer

class GymnasticsCoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymnasticsCoach
        fields = '__all__'
        read_only_fields = ['gym']

class KarateCoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = KarateCoach
        fields = '__all__'
        read_only_fields = ['gym']



class GymnasticsPlayerSerializer(serializers.ModelSerializer):
    gymnastics_coach = serializers.SlugRelatedField(slug_field = 'full_name',queryset=GymnasticsCoach.objects.all())
    
    class Meta:
        model = GymnasticsPlayer
        fields =[ 'full_name',
            'father_name',
            'mother_name',
            'birth_date',
            'phone_number',
            'training_type',
            'weight',
            'gymnastics_coach'
            ]
        read_only_fields = ['gym']
        
class KaratePlayerSerializer(serializers.ModelSerializer):
    karate_coach = serializers.SlugRelatedField(slug_field = 'full_name',queryset=KarateCoach.objects.all())

    class Meta:
        model = KaratePlayer
        fields =[ 'full_name',
            'father_name',
            'mother_name',
            'birth_date',
            'phone_number',
            'training_type',
            'weight',
            'karate_coach'
            ]
        read_only_fields = ['gym']