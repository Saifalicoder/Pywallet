from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from wallet.models import Wallet
from .serializers import UserSerializer
from django.contrib.auth import authenticate
# Create your views here.

# User Signup API
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        # Create wallet for the new user
        Wallet.objects.create(user=user)
        refresh = RefreshToken.for_user(user)
        response =  {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
        return Response(response, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)

        email = data.get("email")
        password = data.get("password")

        # Authenticate user
        user = authenticate(email=email, password=password)
        if not user:
            return Response(
                {"error": "Invalid credentials"},
                status=401,
            )
        refresh = RefreshToken.for_user(user)

        response= {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user':UserSerializer(user).data
        }
        return Response(response)
