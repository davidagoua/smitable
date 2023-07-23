import json

from rest_framework import serializers
from .models import *


class DomicileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domicile
        fields = ['date_debut', 'date_fin', "pays", 'ville', 'commune', 'quartier']


class PatientSerializers(serializers.ModelSerializer):
    domiciles = DomicileSerializer(many=True)

    def create(self, validated_data: dict):
        domiciles = validated_data.pop('domiciles')
        patient = Patient.objects.create(**validated_data)
        for domicile in domiciles:
            Domicile.objects.create(patient=patient, **domicile)
        return patient

    class Meta:
        model = Patient
        exclude = []


class ConstanteSerializers(serializers.ModelSerializer):
    consultation_id = serializers.IntegerField()

    class Meta:
        model = Constante
        fields = ('temperature', 'poids', 'taille', 'pouls', 'tension', 'imc','pression_arterielle','frequence_respiratoire',
                  'imc_status', 'temperature_status', 'tension_status', 'consultation_id', 'id', 'pouls_status')


class ServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id','nom','consultation_count','user','icon','description']


class ConsultationSerializers(serializers.ModelSerializer):
    constante_set = ConstanteSerializers(many=True, label='contantes', read_only=True, allow_null=True)
    patient_id = serializers.IntegerField()
    patient = PatientSerializers(read_only=True)
    service_id = serializers.IntegerField(allow_null=True)
    service = ServiceSerializers(read_only=True)

    class Meta:
        model = Consultation
        fields = '__all__'


class PatientDetailSerializers(serializers.ModelSerializer):
    consultation_set = ConsultationSerializers(many=True, label='consultations', )
    domiciles = DomicileSerializer(many=True)

    def create(self, validated_data):
        consultations_data = validated_data.pop('consultation_set')
        patient = Patient.objects.create(**validated_data)
        for consultation_data in consultations_data:
            Consultation.objects.create(patient=patient, **consultation_data)
        return patient

    class Meta:
        model = Patient
        exclude = []


class RendezVousSerializer(serializers.ModelSerializer):
    patient = PatientSerializers(read_only=True)
    patient_id = serializers.IntegerField()

    class Meta:
        model = RendezVous
        fields = '__all__'



class BoxHospitalisationSerializer(serializers.ModelSerializer):
    chambre = serializers.StringRelatedField()
    class Meta:
        model = BoxHospitalisation
        fields = '__all__'


class ChambreHospitalisation(serializers.ModelSerializer):
    boxes = BoxHospitalisationSerializer(many=True)
    class Meta:
        model = ChambreHospitalisation
        fields = '__all__'

class UniteHospitalisationSerializer(serializers.ModelSerializer):
    chambres = ChambreHospitalisation(many=True)

    class Meta:
        model = UniteHospitalisation
        fields = ['chambres','nom','id']


class HospitalisationSerializer(serializers.ModelSerializer):
    patient = PatientSerializers(read_only=True)
    patient_id = serializers.IntegerField()

    class Meta:
        model = Hospitalisation
        fields = '__all__'


class LoginResponseSerializer(serializers.ModelSerializer):

    groups = serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = ('username', 'email','role','permissions','groups')