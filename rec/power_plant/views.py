# Default import
from django.shortcuts import render
from django.http import Http404

# DRF import
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

# Model, Serializer import
from .models import PowerPlant
from .serlializers import PowerPlantSerializer

class PowerPlantListAPI(APIView):
    def get(self, request):
        queryset = PowerPlant.objects.all()
        serializer = PowerPlantSerializer(queryset, many=True)
        return Response(serializer.data)
    
class PowerPlantAPI(APIView):
    def get(self, request, pk):
        query = PowerPlant.objects.get(pk=pk)
        serializer = PowerPlantSerializer(query)
        return Response(serializer.data)
        