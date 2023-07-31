from django.shortcuts import render
from personel import models
from rest_framework import viewsets, generics
from personel import serializers



class GardeUniteViewSet(generics.ListCreateAPIView):
    queryset = models.GardeUnite.objects.all()
    serializer_class = serializers.GardUnite


class GardeUniteDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.GardeUnite.objects.all()
    serializer_class = serializers.GardUnite


class GardeTourViewSet(generics.ListCreateAPIView):
    queryset = models.GardeTour.objects.all()
    serializer_class = serializers.GardeTour


class GardeTourDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.GardeTour.objects.all()
    serializer_class = serializers.GardeTour