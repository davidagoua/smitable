import random
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


def get_random_code() -> str:
    return f'SMT-{random.randint(100, 999)}'


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    details = models.JSONField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True


class Service(models.Model):
    nom = models.CharField(max_length=225)
    icon = models.CharField(max_length=225, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nom


class Patient(TimestampedModel):
    situation_matrimoniales_choices = [
        ('Celibataire', 'Celibataire'),
        ('Marie', 'Marié'),
        ('Divorce', 'Divorcé'),
        ('Veuf', 'Veuf'),
        ('Autre', 'Autre'),
    ]

    nom = models.CharField(max_length=225)
    prenoms = models.CharField(max_length=225)
    contact = models.CharField(max_length=225)
    situation_matrimoniale = models.CharField(max_length=225, choices=situation_matrimoniales_choices)
    lieu_naissance = models.CharField(max_length=200)
    date_naissance = models.DateField()
    genre = models.CharField(max_length=10, choices=[('M', 'Homme'), ('F', 'Femme')], default='M')
    nationalite = models.CharField(max_length=200)
    ville = models.CharField(max_length=100, null=True, blank=True)
    commune = models.CharField(max_length=100, null=True, blank=True)
    quartier = models.CharField(max_length=100, null=True, blank=True)
    code_patient = models.CharField(max_length=100, blank=True)
    status = models.PositiveIntegerField(default=0)
    profession = models.CharField(max_length=100, null=True, blank=True)

    def save(
            self, *args, **kwargs
    ):
        self.code_patient = get_random_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.prenoms} {self.nom}'


class Consultation(TimestampedModel):
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    mode_entree = models.CharField(max_length=100,
                                   choices=[('Consultation', 'Consultation'), ('Urgence', 'Urgence'),
                                            ('Transfert', 'Transfert'), ('Hospitalisation', 'Hospitalisation'),
                                            ('Autre', 'Autre')],
                                   default='Consultation'
                                   )
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.PositiveIntegerField(default=0)
    motifs = models.JSONField(null=True, blank=True)
    antecedents = models.JSONField(null=True, blank=True)


class MotifConsultation(models.Model):
    consultation = models.ForeignKey('Consultation', on_delete=models.CASCADE)
    motif = models.CharField(max_length=225)
    date = models.DateField(null=True, blank=True)


class Antecedent(models.Model):
    consultation = models.ForeignKey('Consultation', on_delete=models.CASCADE)
    antecedent = models.CharField(max_length=225)
    date = models.DateField(null=True, blank=True)


class Constante(TimestampedModel):
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    temperature = models.FloatField(default=36)
    poids = models.FloatField(default=0)
    taille = models.FloatField(default=0)
    pouls = models.FloatField(default=0)
    tension = models.FloatField(default=0)

    def __str__(self):
        return f'{self.consultation.patient} {self.temperature}'

    @property
    def imc(self):
        return self.poids / ((self.taille / 100) * (self.taille / 100))

    @property
    def imc_status(self):
        if self.imc < 18.5:
            return 'Maigreur'
        elif self.imc >= 18.5 and self.imc <= 24.9:
            return 'Normal'
        elif self.imc >= 25 and self.imc <= 29.9:
            return 'Surpoids'
        elif self.imc >= 30 and self.imc <= 34.9:
            return 'Obésité modérée'
        elif self.imc >= 35 and self.imc <= 39.9:
            return 'Obésité sévère'
        elif self.imc >= 40:
            return 'Obésité morbide'

    @property
    def tension_status(self):
        if self.tension < 9:
            return 'Hypotension'
        elif self.tension >= 9 and self.tension <= 13:
            return 'Tension normale'
        elif self.tension >= 14 and self.tension <= 16:
            return 'Hypertension modérée'
        elif self.tension >= 17 and self.tension <= 20:
            return 'Hypertension sévère'
        elif self.tension >= 21:
            return 'Hypertension très sévère'

    @property
    def pouls_status(self):
        if self.pouls < 60:
            return 'Bradycardie'
        elif self.pouls >= 60 and self.pouls <= 100:
            return 'Normal'
        elif self.pouls >= 101:
            return 'Tachycardie'

    @property
    def temperature_status(self):
        if self.temperature < 36:
            return 'Hypothermie'
        elif self.temperature >= 36 and self.temperature <= 37.5:
            return 'Normal'
        elif self.temperature >= 37.6 and self.temperature <= 38.5:
            return 'Fièvre modérée'
        elif self.temperature >= 38.6 and self.temperature <= 40:
            return 'Fièvre élevée'
        elif self.temperature >= 40.1:
            return 'Hyperthermie'


class RendezVous(TimestampedModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField()
    state = models.PositiveIntegerField(default=0)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)


