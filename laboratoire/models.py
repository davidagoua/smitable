from django.db import models
import core.models as core_models


class TypeAnalyse(models.Model):
    nom = models.CharField(max_length=100)


class TechniqueAnalyse(models.Model):
    nom = models.CharField(max_length=100)


class AnalyseRapide(core_models.TimestampedModel):
    patient = models.ForeignKey(core_models.Patient, on_delete=models.CASCADE)
    type_analyse = models.ForeignKey(TypeAnalyse, on_delete=models.SET_NULL, null=True)
    technique_analyse = models.ForeignKey(TechniqueAnalyse, on_delete=models.SET_NULL, null=True)
    resultat = models.BooleanField(default=False)
    consultation = models.ForeignKey(core_models.Consultation, on_delete=models.SET_NULL, null=True)


class Analyse(models.Model):
    nom = models.CharField(max_length=200)


class ProtocolAnalyse(models.Model):
    nom = models.CharField(max_length=200)
    duree_month = models.PositiveIntegerField(default=1)
    data = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f'protocole {self.nom}'


class AnalysePatient(core_models.TimestampedModel):
    type_analyse = models.ForeignKey(TypeAnalyse, on_delete=models.SET_NULL, null=True)
    technique_analyse = models.ForeignKey(TechniqueAnalyse, on_delete=models.SET_NULL, null=True)
    patient = models.ForeignKey(core_models.Patient, on_delete=models.SET_NULL, null=True)
    analyse = models.ForeignKey(Analyse, on_delete=models.CASCADE, null=True)
    resultat = models.IntegerField(default=0)
    state = models.PositiveIntegerField(default=0)
    consultation = models.ForeignKey(core_models.Consultation, on_delete=models.CASCADE, null=True)