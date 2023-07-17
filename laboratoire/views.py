from django.shortcuts import render
from rest_framework import generics
from .serializers import TypeAnalyseSerializers, TechniqueAnalyseSerializers, AnalyseRapideSerializers, \
    ProtocolAnalyseSerializer, AnalyseSerializer, AnalysePatientSerializer
from .models import TypeAnalyse, TechniqueAnalyse, AnalyseRapide, ProtocolAnalyse, Analyse, AnalysePatient


class TypeAnalyseListView(generics.ListAPIView):
    serializer_class = TypeAnalyseSerializers
    queryset = TypeAnalyse.objects.all()


class TechniqueAnalyseListView(generics.ListAPIView):
    serializer_class = TechniqueAnalyseSerializers
    queryset = TechniqueAnalyse.objects.all()


class AnalyseRapideListView(generics.ListCreateAPIView):
    serializer_class = AnalyseRapideSerializers
    queryset = AnalyseRapide.objects.all()


class ProtocolAnalyseListView(generics.ListAPIView):
    serializer_class = ProtocolAnalyseSerializer
    queryset = ProtocolAnalyse.objects.all()


class AnalyseListView(generics.ListAPIView):
    serializer_class = AnalyseSerializer
    queryset = Analyse.objects.all()


class AnalysePatientListView(generics.ListCreateAPIView):
    serializer_class = AnalysePatientSerializer
    queryset = AnalysePatient.objects.all()