from rest_framework import serializers
from .models import Subscription
from gym_core.models import GymnasticsPlayer,KaratePlayer

class SubscriptionSerializer(serializers.ModelSerializer):
    player_name = serializers.ReadOnlyField(source='active_player.full_name')
    training_display = serializers.ReadOnlyField(source='active_player.get_training_type_display')

    class Meta:
        model = Subscription
        fields = [
            'id',
            'gym', 
            'gymnastics_player',  
            'karate_player',     
            'player_name', 
            'training_display', 
            'start_date', 
            'end_date', 
            'price', 
            'is_paid'
        ]
        read_only_fields = ['gym']
        
    def validate(self, data):
        gym_p = data.get('gymnastics_player')
        karate_p = data.get('karate_player')
        if not gym_p and not karate_p:
            raise serializers.ValidationError({"player": "يجب اختيار لاعب واحد على الأقل (جمباز أو كاراتيه)"} )
        if gym_p and karate_p:
            raise serializers.ValidationError({"player": "لا يمكن اختيار لاعب جمباز ولاعب كاراتيه في نفس الاشتراك، اختر أحدهما فقط"})
        return data
    