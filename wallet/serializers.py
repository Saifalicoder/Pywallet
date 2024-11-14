
from rest_framework import serializers
from .models import  Wallet, Transaction
from user.serializers import UserSerializer

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['user', 'balance','is_enabled']

class TransactionSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Transaction
        fields = ['user', 'amount', 'transaction_type', 'date']