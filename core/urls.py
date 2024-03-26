from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PatientApiListView, PatientApiDetailView, ConsultationApiListView, ServiceListView, \
    ConstanteApiListView, ServiceConsultationListView, RendezVousListView, HospitalisationListView, \
    UniteHospitalisationListView, StatistiqueView, ConsultationApiCreateView, BilanInitialView, BilanInitialListView, \
     UrgenceApiListView, ProfessionViewset
from core import views
from core import nfviews


router = DefaultRouter()
router.register('professions', ProfessionViewset, basename='professions')

urlpatterns = [
    path('', include(router.urls)),
    path('patients/', views.PatientApiListView.as_view()),
    path('patients-paginate/', nfviews.PatientApiListView.as_view()),
    path('patients/<int:pk>/', PatientApiDetailView.as_view()),
    path('consultations/', ConsultationApiListView.as_view()),
    path('consultations_urgence/', UrgenceApiListView.as_view()),
    path('services/', ServiceListView.as_view()),
    path('constantes/', ConstanteApiListView.as_view()),
    path('rdv/', RendezVousListView.as_view()),
    path('unites/', UniteHospitalisationListView.as_view()),
    path('boxes/', views.get_boxes),
    path('suivre/<int:pk>/', views.suivre_patient),
    path('hospitalisations/', HospitalisationListView.as_view()),
    path('hospitalisations/<int:pk>/', views.HospitalisationUpdateView.as_view()),
    path('services/<int:service_id>/consultations/', ServiceConsultationListView.as_view()),
    path('statistiques/', StatistiqueView.as_view()),
    path('consultations/<int:pk>/', ConsultationApiCreateView.as_view(),),
    path('bilan-initial/<int:pk>/', BilanInitialView.as_view(),),
    path('bilan-initial/', BilanInitialListView.as_view(),),
    path('upload-patient/', nfviews.UploadPatientView.as_view(),),
    path('dossier-data/<str:collection>/', views.DossierDataAPIView.as_view()),
    path('dossier-data/<str:collection>/<int:pk>/', views.DossierDataAPIView.as_view()),
    path('users/', views.UserListView.as_view()),
    path('users/<int:pk>/', views.UserRetrieveView.as_view()),
    path('groups/', views.GroupListView.as_view()),
    path('permissions/', views.PermissionListView.as_view()),
    path('upload-patient-file/', views.upload_patient_file, name='upload-patient-file')
]