from rest_framework import serializers
from .models import User
from club.models import Gym

class UserSerializer(serializers.ModelSerializer):
    gym_name = serializers.CharField(write_only=True,required=True)
    class Meta:
        
        model = User
        fields = ['username','full_name','email','password','gym_name']
        extra_kwargs = {'password':{'write_only':True}}
    #للتعامل مع البيانات وتشفير كلمة المرور
    def create(self,validated_data):
            gym_name = validated_data.pop('gym_name')
            gym = Gym.objects.create(name=gym_name)
            user = User.objects.create_user(gym = gym,**validated_data)
            user.is_staff = True
            #user.is_superuser = True
            user.save()
            return user
    #لتحديث البيانات
    def update(self, instance, validated_data):
        password= validated_data.pop('password',None)
        for attr , value in validated_data.items():
             setattr(instance,attr,value)
        if password:
             instance.set_password(password)
        instance.save()
        return instance
    
class ChangePasswordSerializer(serializers.Serializer):
     old_password = serializers.CharField(required=True)
     new_password = serializers.CharField(required=True)

     def validate_old_password(self,value):
          user = self.context['request'].user
          if not user.check_password(value):
               raise serializers.ValidationError("Invalid old password")
          return value
     
class AddManagerSerializer(serializers.ModelSerializer):
     class Meta:
          model = User
          fields = ['username','full_name','email','password']
          extra_kwargs= {'password':{'write_only':True}}
     def create(self, validated_data):
          password = validated_data.pop('password')
          current_user = self.context['request'].user
          gym_of_current_user = current_user.gym
          user = User.objects.create_user(password=password, gym = gym_of_current_user,is_staff=True,**validated_data)
          return user
