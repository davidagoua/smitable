from django.urls import path, include
from pharmacy import views


urlpatterns = [
    path('medicaments/', views.MedicamentListView.as_view()),
    path('ordonances/', views.OrdonanceListView.as_view()),
    path('molecules/', views.MoleculeListView.as_view()),
    path('categorie_molecules/', views.CategorieMoleculeListView.as_view()),
    path('protocoles/', views.ProtocolListView.as_view()),
    path('upload-produit/', views.UploadProduit.as_view())
]