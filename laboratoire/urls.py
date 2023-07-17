from django.urls import path, include
from .views import TypeAnalyseListView, TechniqueAnalyseListView, AnalyseRapideListView, ProtocolAnalyseListView, \
    AnalyseListView, AnalysePatientListView, AnalysePatientApiView

urlpatterns = [
    path('type-analyses/', TypeAnalyseListView.as_view()),
    path('technique-analyses/', TechniqueAnalyseListView.as_view()),
    path('analyse-rapide/', AnalyseRapideListView.as_view()),
    path('protocol-analyses/', ProtocolAnalyseListView.as_view()),
    path('analyses/', AnalyseListView.as_view()),
    path('analyse-patient/', AnalysePatientListView.as_view()),
    path('analysepatient/', AnalysePatientApiView.as_view()),
]