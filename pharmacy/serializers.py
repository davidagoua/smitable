import json

from rest_framework import serializers
from core import serializers as core_serializers
from pharmacy import models


class ProduitSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Produit
        fields = '__all__'


class LigneOrdonanceSerializer(serializers.ModelSerializer):
    produit = ProduitSerializer(read_only=True)
    class Meta:
        model = models.LigneOrdonance
        fields = ['produit_id','quantite','produit']


class OrdonanceSerializer(serializers.ModelSerializer):
    lignes = LigneOrdonanceSerializer(many=True)
    consultation_id = serializers.IntegerField()
    consultation = core_serializers.ConsultationSerializers(read_only=True)

    def create(self, validated_data):
        ligne_ordonance_set = validated_data.pop('lignes')
        print(ligne_ordonance_set)
        ordonance = models.Ordonance.objects.create(**validated_data)
        for ligne in ligne_ordonance_set:
            print(ligne)
            models.LigneOrdonance.objects.create(ordonance=ordonance, **ligne)
        return ordonance
    class Meta:
        model = models.Ordonance
        fields = ['consultation','nombre_produit','prix_total','lignes','created_at','consultation_id']



class MoleculeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Molecule
        fields = '__all__'


class CategorieMoleculeSerializer(serializers.ModelSerializer):
    molecules = MoleculeSerializer(many=True)
    class Meta:
        model = models.CategorieMolecule
        fields = '__all__'


class ProtocolSerializer(serializers.ModelSerializer):
    molecules_id = serializers.ListField(child=serializers.IntegerField(), write_only=True)
    molecules = MoleculeSerializer(many=True, read_only=True)
    patient_id = serializers.IntegerField()
    patient = core_serializers.PatientSerializers(read_only=True)


    def create(self, validated_data):
        molecules = validated_data.pop('molecules_id')
        protocol = models.Protocol.objects.create(**validated_data)
        for molecule in molecules:
            molecule = models.Molecule.objects.get(id=molecule)
            protocol.molecules.add(molecule)
        return protocol
    class Meta:
        model = models.Protocol
        fields = '__all__'