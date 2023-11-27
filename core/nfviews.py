from rest_framework.views import APIView
from rest_framework.response import Response
from core.services import protocol


class UploadPatientView(APIView):

    def get(self, request):
        return Response(data={"message":"Ok"})

    def post(self, request):
        fichier = request.FILES.get('fichier', None)
        protocol.CreatePatient().from_excel_file(fichier)
        return Response(data={"success": request.POST.get('name',None)})