from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from wallet.models import Wallet, Transaction
from wallet.serializers import  WalletSerializer, TransactionSerializer
from .serializers import UserSerializer
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