from rest_framework import serializers
from .models import Schedule ,Equipment
from gym_core.models import *

class ScheduleSerializer(serializers.ModelSerializer):
    day_display = serializers.ReadOnlyField(source='get_day_display')
    coach_name = serializers.ReadOnlyField(source='active_coach.full_name')
    gymnastics_player_names = serializers.SlugRelatedField(source='gymnastics_players', many=True, read_only=True, slug_field='full_name')
    karate_player_names = serializers.SlugRelatedField(source='karate_players', many=True, read_only=True, slug_field='full_name')

    class Meta:
        model = Schedule
        fields = [
            'id', 
            'gym',
            'day', 
            'day_display',
            'start_time', 
            'end_time', 
            'gymnastics_coach',    
            'karate_coach',        
            'coach_name',
            'gymnastics_players',  
            'karate_players',      
            'gymnastics_player_names',
            'karate_player_names',
        ]
        read_only_fields = ['gym']

    def validate(self, data):
        gym_c = data.get('gymnastics_coach')
        karate_c = data.get('karate_coach')
        if gym_c and karate_c:
            raise serializers.ValidationError( {"coach": "لا يمكن تعيين مدرب جمباز ومدرب كاراتيه في نفس الحصة"})
        if not gym_c and not karate_c:
            raise serializers.ValidationError( {"coach": "يجب تعيين مدرب واحد على الأقل للحصة"} )
        return data

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['id','gym','name', 'quantity', 'price', 'last_updated']
        read_only_fields = ['gym']


class PublicEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['id', 'name']        