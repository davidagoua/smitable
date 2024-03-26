from django.contrib import admin
from .models import Patient, Consultation, Constante, Service, Hospitalisation, UniteHospitalisation, \
    RendezVous, User
from core import models
from django.contrib.auth.admin import UserAdmin



@admin.register(User)
class CoreUserAdmin(UserAdmin):
    list_display = ['pk','username', 'role', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser']

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = [
        'id','created_at','code_patient','status',
        'nom','prenoms','date_naissance','lieu_naissance'
    ]
    search_fields = [
        'code_patient','nom'
    ]


@admin.register(Constante)
class ConstanteAdmin(admin.ModelAdmin):
    list_display = ['consultation', 'temperature']

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


@admin.register(UniteHospitalisation)
class UniteHospitalisationAdmin(admin.ModelAdmin):
    list_display = ['nom']


class BoxHospitalisationAdmin(admin.TabularInline):
    list_display = ['nom','capacite','occuper']
    model = models.BoxHospitalisation


@admin.register(models.ChambreHospitalisation)
class ChambreHospitalisation(admin.ModelAdmin):
    list_display = ['nom']
    inlines = [BoxHospitalisationAdmin]

@admin.register(Hospitalisation)
class HospitalisationAdmin(admin.ModelAdmin):
    list_display = ['patient']


@admin.register(RendezVous)
class RendezvousAdmin(admin.ModelAdmin):
    list_display = ['patient', 'service', 'date']


