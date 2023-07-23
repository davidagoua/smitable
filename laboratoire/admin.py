from django.contrib import admin
from .models import TypeAnalyse, TechniqueAnalyse, AnalyseRapide, ProtocolAnalyse, Analyse, AnalysePatient, Laboratoire


@admin.register(TypeAnalyse)
@admin.register(Analyse)
@admin.register(Laboratoire)
@admin.register(TechniqueAnalyse)
class TypeAnalyseAdmin(admin.ModelAdmin):
    list_display = ['nom']


@admin.register(AnalyseRapide)
class AnalyseRapideAdmin(admin.ModelAdmin):
    list_display = ['patient', 'resultat']


@admin.register(ProtocolAnalyse)
class ProtocolAnalyseAdmin(admin.ModelAdmin):
    list_display = ['nom','duree_month']


@admin.register(AnalysePatient)
class AnalysePatientAdmin(admin.ModelAdmin):
    list_display = ['patient','analyse','resultat','state','code_barre']
