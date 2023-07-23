from django.shortcuts import render
from rest_framework import generics, views, response
from .serializers import TypeAnalyseSerializers, TechniqueAnalyseSerializers, AnalyseRapideSerializers, \
    ProtocolAnalyseSerializer, AnalyseSerializer, AnalysePatientSerializer, LaboratoireSerializer
from .models import TypeAnalyse, TechniqueAnalyse, AnalyseRapide, ProtocolAnalyse, Analyse, AnalysePatient, Laboratoire


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
    queryset = AnalysePatient.objects.prefetch_related('patient')

    def get_queryset(self):
        state = self.request.GET.get('state', 0)
        return self.queryset.filter(state=state)


class AnalysePatientUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnalysePatientSerializer
    queryset = AnalysePatient.objects.all()




class AnalysePatientApiView(views.APIView):

    def get(self, request):
        analyse_patients = AnalysePatient.objects.all()

        return response.Response(
            AnalysePatientSerializer(analyse_patients, many=True).data
        )

    def post(self, request):
        analyse_patient = AnalysePatient.objects.create(
            patient_id= request.POST.get('patient_id'),
            type_analyse_id= request.POST.get('type_analyse_id'),
            technique_analyse_id= request.POST.get('technique_analyse_id'),
            consultation_id= request.POST.get('consultation_id')
        )

        return response.Response('ok')


class LaboratoireListView(generics.ListCreateAPIView):
    serializer_class = LaboratoireSerializer
    queryset = Laboratoire.objects.all()