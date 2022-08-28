from dataclasses import field
from rest_framework import serializers
from .models import PowerPlant

class PowerPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerPlant
        fields = '__all__'