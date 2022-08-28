from dataclasses import field
from re import search
from rest_framework import serializers
from .models import Bank, BankAccount

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        field = '__all__'