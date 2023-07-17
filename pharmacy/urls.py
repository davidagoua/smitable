from django.urls import path, include
from pharmacy import views


urlpatterns = [
    path('medicaments/', views.MedicamentListView.as_view()),
    path('ordonances/', views.OrdonanceListView.as_view()),
]