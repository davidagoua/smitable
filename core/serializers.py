from rest_framework import serializers
from .models import *


class PatientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Patient
        exclude = []


class ConstanteSerializers(serializers.ModelSerializer):
    consultation_id = serializers.IntegerField()

    class Meta:
        model = Constante
        fields = ('temperature', 'poids', 'taille', 'pouls', 'tension', 'imc',
                  'imc_status', 'temperature_status','tension_status',  'consultation_id', 'id', 'pouls_status')


class ConsultationSerializers(serializers.ModelSerializer):
    constante_set = ConstanteSerializers(many=True, label='contantes', read_only=True, allow_null=True)
    patient_id = serializers.IntegerField()
    patient = PatientSerializers(read_only=True)
    motifs = serializers.StringRelatedField(many=True)
    antecedents = serializers.StringRelatedField(many=True)

    class Meta:
        model = Consultation
        fields = '__all__'


class PatientDetailSerializers(serializers.ModelSerializer):
    consultation_set = ConsultationSerializers(many=True, label='consultations', )

    def create(self, validated_data):
        consultations_data = validated_data.pop('consultation_set')
        patient = Patient.objects.create(**validated_data)
        for consultation_data in consultations_data:
            Consultation.objects.create(patient=patient, **consultation_data)
        return patient

    class Meta:
        model = Patient
        exclude = []


class ServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class RendezVousSerializer(serializers.ModelSerializer):
    patient = PatientSerializers(read_only=True)
    patient_id = serializers.IntegerField()

    class Meta:
        model = RendezVous
        fields = '__all__'