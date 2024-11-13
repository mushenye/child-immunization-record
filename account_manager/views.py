from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.request import Request
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        token['username']=user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class Register(APIView):

    def post(self, request:Request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            user.set_password(serializer.validated_data['password'])
            user.save()

            refresh = RefreshToken.for_user(user)
        
            response = {
                'message': 'User created',
                'data':serializer.data,
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data={'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request, format=None):
        data = request.data

        email = data.get('email', None)
        password = data.get('password', None)

        user = authenticate(email=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                response = {
                'message': 'Login successful',
                
             }
                return Response(data=response, status=status.HTTP_200_OK)
  
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

# class LoginView(APIView):
#     def post(self, request, *args, **kwargs):
#         username = request.data.get("username")
#         password = request.data.get("password")
        
#         user = authenticate(username=username, password=password)
        
#         if user is not None:
#             # Generate JWT tokens
#             refresh = RefreshToken.for_user(user)
            
#             response = {
#                 'message': 'Login successful',
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token)
#             }
#             return Response(data=response, status=status.HTTP_200_OK)
        
#         return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)



class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()  # Blacklist the token to prevent future use

            return Response({"message": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": "Invalid token or logout failed"}, status=status.HTTP_400_BAD_REQUEST)
        



