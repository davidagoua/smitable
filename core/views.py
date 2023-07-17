from django.shortcuts import render
from rest_framework import viewsets, views, generics, filters, permissions
from django_filters import rest_framework
from django.contrib.auth import login
from rest_framework.authentication import TokenAuthentication
from .serializers import PatientSerializers, \
    PatientDetailSerializers, ConsultationSerializers, ConstanteSerializers, \
    ServiceSerializers, RendezVousSerializer, HospitalisationSerializer, UniteHospitalisationSerializer, \
    DomicileSerializer
from core.models import Patient, Consultation, Constante, Service, RendezVous, Hospitalisation, \
    UniteHospitalisation, Domicile


class PatientApiListView(generics.ListCreateAPIView):
    serializer_class = PatientSerializers
    queryset = Patient.objects.all()
    authentication_classes = [TokenAuthentication]
    # permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    filterset_fields = ('code_patient', 'nom', 'prenoms')
    search_fields = ['nom', 'prenoms', 'code_patient']


class PatientApiDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientDetailSerializers
    queryset = Patient.objects.all()


class ConsultationApiListView(generics.ListCreateAPIView):
    serializer_class = ConsultationSerializers
    queryset = Consultation.objects.all()


class ConstanteApiListView(generics.ListCreateAPIView):
    serializer_class = ConstanteSerializers
    queryset = Constante.objects.all()


class ServiceListView(generics.ListAPIView):
    serializer_class = ServiceSerializers
    queryset = Service.objects.all()


class ServiceConsultationListView(generics.ListAPIView):
    serializer_class = ConsultationSerializers

    def get_queryset(self):
        return Consultation.objects.filter(service_id=self.kwargs['service_id'])


class RendezVousListView(generics.ListCreateAPIView):
    serializer_class = RendezVousSerializer
    queryset = RendezVous.objects.filter(state=0)


class UniteHospitalisationListView(generics.ListCreateAPIView):
    serializer_class = UniteHospitalisationSerializer
    queryset = UniteHospitalisation.objects.all()


class HospitalisationListView(generics.ListCreateAPIView):
    serializer_class = HospitalisationSerializer
    queryset = Hospitalisation.objects.all()
