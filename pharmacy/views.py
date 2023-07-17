from django.shortcuts import render
from rest_framework.viewsets import generics
from pharmacy import serializers, models


class MedicamentListView(generics.ListCreateAPIView):
    queryset = models.Produit.objects.all()
    serializer_class = serializers.ProduitSerializer


class OrdonanceListView(generics.ListCreateAPIView):
    queryset = models.Ordonance.objects.all()
    serializer_class = serializers.OrdonanceSerializer