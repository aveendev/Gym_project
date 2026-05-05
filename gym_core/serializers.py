

from rest_framework import serializers
from .models import Coach,Playar

class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fieldes = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playar
        fieldes = '__all__'