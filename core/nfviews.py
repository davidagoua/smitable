from rest_framework.views import APIView
from rest_framework.response import Response
from core.services import protocol
from threading import Thread


class UploadPatientView(APIView):

    def get(self, request):
        return Response(data={"message":"Ok"})

    def post(self, request):
        fichier = request.FILES.get('fichier', None)
        Thread(target=protocol.CreatePatient.from_excel_file, args=(fichier, )).start()
        return Response(data={"success": request.POST.get('name',None)})