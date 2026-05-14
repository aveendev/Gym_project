from urllib.request import Request

from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import ChangePasswordSerializer, UserSerializer


# Create your views here.
#واجهة تسجيل دخول المدير
class LoginView(TokenObtainPairView):
    permission_classes = [AllowAny]

#واجهة انشاء حساب مدير جديد
class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post (self , request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(is_staff = True, is_superuser = True)
            return Response({"message":"Account created successfully"},status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
#عرض وتعديل الملف الشخصي
class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        return self.request.user
    
#تغيير كلمة المرور
class ChangePassword(generics.UpdateAPIView):
    serializer_class= ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    def update(self, request, *args, **kwargs):
        serializer =  self.get_serializer(data = request.data)
        if serializer.is_valid():
            self.request.user.set_password(serializer.validated_data['new_password'])
            self.request.user.save()
            return Response({"detail":"Password changed successfully"},status=status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)