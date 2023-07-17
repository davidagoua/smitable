from django.urls import path, include
from .views import PatientApiListView, PatientApiDetailView, ConsultationApiListView, ServiceListView, \
    ConstanteApiListView, ServiceConsultationListView, RendezVousListView


urlpatterns = [
    path('patients/', PatientApiListView.as_view()),
    path('patients/<int:pk>/', PatientApiDetailView.as_view()),
    path('consultations/', ConsultationApiListView.as_view()),
    path('services/', ServiceListView.as_view()),
    path('constantes/', ConstanteApiListView.as_view()),
    path('rdv/', RendezVousListView.as_view()),
    path('services/<int:service_id>/consultations/', ServiceConsultationListView.as_view())
]