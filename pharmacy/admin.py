from django.contrib import admin
from pharmacy import models


@admin.register(models.Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ['nom','prix','type']


@admin.register(models.TypeProduits)
@admin.register(models.CategoryProduits)
class TypeProduitAdmin(admin.ModelAdmin):
    list_display = ['nom']


@admin.register(models.Ordonance)
class Ordonance(admin.ModelAdmin):
    list_display = ['consultation']