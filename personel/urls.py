from personel import views
from django.urls import path



urlpatterns = [
    path('garde_unites/', views.GardeUniteViewSet.as_view()),
    path('garde_unites/<int:pk>/', views.GardeUniteDetailViewSet.as_view()),
    path('garde_tours/', views.GardeTourViewSet.as_view()),
    path('garde_tours/<int:pk>/', views.GardeTourDetailViewSet.as_view()),
]