from django.urls import path, include
from .views import PatientApiListView, PatientApiDetailView, ConsultationApiListView, ServiceListView, \
    ConstanteApiListView, ServiceConsultationListView, RendezVousListView, HospitalisationListView, \
    UniteHospitalisationListView, StatistiqueView, ConsultationApiCreateView, BilanInitialView, BilanInitialListView, \
    UploadPatient, UrgenceApiListView
from core import views

urlpatterns = [
    path('patients/', PatientApiListView.as_view()),
    path('patients/<int:pk>/', PatientApiDetailView.as_view()),
    path('consultations/', ConsultationApiListView.as_view()),
    path('consultations_urgence/', UrgenceApiListView.as_view()),
    path('services/', ServiceListView.as_view()),
    path('constantes/', ConstanteApiListView.as_view()),
    path('rdv/', RendezVousListView.as_view()),
    path('unites/', UniteHospitalisationListView.as_view()),
    path('boxes/', views.get_boxes),
    path('hospitalisations/', HospitalisationListView.as_view()),
    path('hospitalisations/<int:pk>/', views.HospitalisationUpdateView.as_view()),
    path('services/<int:service_id>/consultations/', ServiceConsultationListView.as_view()),
    path('statistiques/', StatistiqueView.as_view()),
    path('consultations/<int:pk>/', ConsultationApiCreateView.as_view(),),
    path('bilan-initial/<int:pk>/', BilanInitialView.as_view(),),
    path('bilan-initial/', BilanInitialListView.as_view(),),
    path('upload-patient/', UploadPatient.as_view(),),
    path('dossier-data/<str:collection>/', views.DossierDataAPIView.as_view()),
    path('dossier-data/<str:collection>/<int:pk>/', views.DossierDataAPIView.as_view()),
]