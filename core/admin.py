from django.contrib import admin
from .models import Patient, Consultation, Constante, Service


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = [
        'created_at','code_patient','status',
        'nom','prenoms','date_naissance','lieu_naissance'
    ]


class ConsultationTabularInline(admin.TabularInline):
    model = Constante
    list_display = [
        'temperature','poids','taille'
    ]


@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = [
        'created_at','patient','service'
    ]
    inlines = [ConsultationTabularInline]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = [
        'pk', 'nom','icon'
    ]