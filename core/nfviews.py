from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response

from core import serializers
from core.models import Patient
from core.services import protocol
from threading import Thread

from core.views import DefaultPaginatorClass


class UploadPatientView(APIView):

    def get(self, request):
        return Response(data={"message":"Ok"})

    def post(self, request):
        print('starting')
        fichier = request.FILES.get('fichier', None)
        #Thread(target=protocol.CreatePatient.from_excel_file, args=(fichier, )).start()
        protocol.CreatePatient.from_excel_file(fichier)
        return Response(data={"success": request.POST.get('name',None)})


class PatientApiListView(generics.ListCreateAPIView):
    serializer_class = serializers.PatientSerializers
    queryset = Patient.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = DefaultPaginatorClass


    def get_queryset(self):
        code_patient = self.request.GET.get('code_patient', '').upper()
        nom = self.request.GET.get('nom', '').upper()
        prenoms = self.request.GET.get('prenoms', '').upper()
        contact = self.request.GET.get('contact', '').upper()
        return self.queryset.filter(
            code_patient__contains=code_patient,
            nom__contains=nom,
            prenoms__contains=prenoms,
            contact__contains=contact,
        )