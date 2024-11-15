from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Wallet, Transaction
from .serializers import  WalletSerializer, TransactionSerializer
from django.db import transaction
# Create your views here.

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def wallet_status(request):
    # Wallet will already be created during signup, just return the wallet data
    wallet = Wallet.objects.get(user=request.user)
    return Response({"status":wallet.is_enabled})

# User Wallet Enable API
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def enable_wallet(request):
    # Wallet will already be created during signup, just return the wallet data
    wallet = Wallet.objects.get(user=request.user)
    wallet.is_enabled = True
    wallet.save()
    return Response({"message":"Wallet Enabled Successfully"})



# Add money to wallet
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_money(request):
    amount =float(request.data.get('amount'))
    print(type(amount))
    print(amount)
    if amount <= 0:
        return Response({"error": "Amount must be positive"}, status=status.HTTP_400_BAD_REQUEST)

    wallet = Wallet.objects.get(user=request.user)
    print(wallet.balance)
    try:
        with transaction.atomic():
            if wallet.is_enabled:
      
                wallet.balance = float(wallet.balance)+amount
             
                wallet.save()
     
                Transaction.objects.create(user=request.user, amount=amount, transaction_type="add")
            else:
                return Response({'error': "wallet is disabled"})
        return Response({'balance': wallet.balance})
    # Record the transaction
    except Exception as e:
            return Response({"error": "Transaction failed", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    


# Remove money from wallet
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def remove_money(request):
    amount = float(request.data.get('amount'))
    if amount <= 0:
        return Response({"error": "Amount must be positive"}, status=status.HTTP_400_BAD_REQUEST)

    wallet = Wallet.objects.get(user=request.user)
    try:
        with transaction.atomic():
            if wallet.is_enabled:
                if wallet.balance < amount:
                    return Response({"error": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST)
                wallet.balance = float(wallet.balance) - amount
                wallet.save()
                # Record the transaction
                Transaction.objects.create(user=request.user, amount=amount, transaction_type="remove")
            else:
                return Response({'error': "wallet is disabled"})
        return Response({'balance': wallet.balance}) 
    except Exception as e:
            return Response({"error": "Transaction failed", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
# User Transaction History API
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def transaction_history(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)

# User Wallet Balance API
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def wallet_balance(request):
    wallet = Wallet.objects.get(user=request.user)
    if wallet.is_enabled:
        return Response({'balance': wallet.balance})
    else:
        return Response({'error': "wallet is disabled"})