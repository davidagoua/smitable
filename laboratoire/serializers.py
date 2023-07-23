from rest_framework import serializers

import core.models
from .models import TypeAnalyse, TechniqueAnalyse, AnalyseRapide, ProtocolAnalyse, Analyse, AnalysePatient, Laboratoire
from core import serializers as core_serializers

class TypeAnalyseSerializers(serializers.ModelSerializer):

    class Meta:
        model = TypeAnalyse
        fields = '__all__'


class TechniqueAnalyseSerializers(serializers.ModelSerializer):

    class Meta:
        model = TechniqueAnalyse
        fields = '__all__'


class AnalyseRapideSerializers(serializers.ModelSerializer):
    technique_analyse_id = serializers.IntegerField()
    technique_analyse = TechniqueAnalyseSerializers(read_only=True)
    type_analyse = TypeAnalyseSerializers(read_only=True)
    type_analyse_id = serializers.IntegerField()
    consultation = core_serializers.ConsultationSerializers(read_only=True)
    consultation_id = serializers.IntegerField(allow_null=True)
    service_id = serializers.IntegerField()
    service = core_serializers.ServiceSerializers(read_only=True)

    def create(self, validated_data: dict):

        # Créez une instance de AnalyseRapide avec les données validées
        analyse = AnalyseRapide.objects.create(**validated_data)

        consultation = core.models.Consultation.objects.get(id=analyse.consultation_id)
        consultation.service_id = analyse.service_id
        consultation.save()

        return analyse

    class Meta:
        model = AnalyseRapide
        fields = '__all__'

class ProtocolAnalyseSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProtocolAnalyse
        fields = '__all__'


class AnalyseSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Analyse


class AnalysePatientSerializer(serializers.ModelSerializer):
    patient_id = serializers.IntegerField()
    patient = core_serializers.PatientSerializers(read_only=True)
    service_id = serializers.IntegerField()
    service = core_serializers.ServiceSerializers(read_only=True)
    class Meta:
        fields = '__all__'
        model = AnalysePatient


class LaboratoireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratoire
        fields='__all__'