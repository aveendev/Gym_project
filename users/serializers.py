from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','full_name','email','password']
        extra_kwargs = {'password':{'write_only':True}}
    #للتعامل مع البيانات وتشفير كلمة المرور
    def create(self,validated_data):
            password = validated_data.pop('password')
            user = User.objects.create_user(**validated_data)
            user.is_staff = True
            user.is_superuser = True
            user.set_password(password)
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
               raise
          serializers.ValidationError("Invaild old password")
          return value