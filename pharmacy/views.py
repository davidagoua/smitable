import openpyxl
from django.core.files.uploadedfile import UploadedFile
from django.shortcuts import render

from django_excel import ExcelMemoryFileUploadHandler
from rest_framework.viewsets import generics
from rest_framework import views, response
from pharmacy import serializers, models


class MedicamentListView(generics.ListCreateAPIView):
    queryset = models.Produit.objects.all()
    serializer_class = serializers.ProduitSerializer


class OrdonanceListView(generics.ListCreateAPIView):
    queryset = models.Ordonance.objects.all()
    serializer_class = serializers.OrdonanceSerializer


class MoleculeListView(generics.ListCreateAPIView):
    queryset = models.Molecule.objects.all()
    serializer_class = serializers.MoleculeSerializer


class CategorieMoleculeListView(generics.ListCreateAPIView):
    queryset = models.CategorieMolecule.objects.all()
    serializer_class = serializers.CategorieMoleculeSerializer


class ProtocolListView(generics.ListCreateAPIView):
    queryset = models.Protocol.objects.all()
    serializer_class = serializers.ProtocolSerializer


class UploadProduit(views.APIView):

    def post(self, request):
        file: ExcelMemoryFileUploadHandler = request.FILES['fichier']
        workbook = openpyxl.load_workbook(file)

        sheet = workbook.active

        models.Produit.objects.bulk_create([
            models.Produit(
                famille= p[0],
                nom= p[1],
                denomination= p[2],
                reference= p[2],
                conditionnement= p[3],
                prix= p[4],
                stock= p[5] if p[5] is not None else 0 ,
                categorie_id=1,
                type_id=1
        ) for p in sheet.iter_rows(min_row=2, values_only=True)
        ])


        return response.Response({
            "file": "ok"
        })
