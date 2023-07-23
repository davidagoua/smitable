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


@admin.register(models.Protocol)
class ProtocolAdmin(admin.ModelAdmin):
    list_display = ['nom','duree_month']


@admin.register(models.Molecule)
class MoleculeAdmin(admin.ModelAdmin):
    list_display = ['pk','nom']


@admin.register(models.CategorieMolecule)
class CategorieMoleculeAdmin(admin.ModelAdmin):
    list_display = ['nom']