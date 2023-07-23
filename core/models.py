import datetime
import random
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver


class User (AbstractUser):
    ADMIN = 0
    MEDECIN = 10
    INFIRMIER = 20
    SAISIR = 30
    HOSPITALISATION = 40
    CONSULTATION = 50
    LABORATOIRE = 60

    ROLE_CHOICES = [
        (ADMIN, 'Administrateur'),
        (MEDECIN, 'Medecin'),
        (INFIRMIER, 'Infirmier'),
        (SAISIR, 'Saisir'),
        (HOSPITALISATION, 'Hospitalisation'),
        (CONSULTATION, 'Consultation'),
        (LABORATOIRE, 'Laboratoire'),
    ]

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    contact = models.CharField(max_length=100, null=True, blank=True)

    @property
    def permissions(self):
        return self.get_all_permissions()



def get_random_code() -> str:
    return str(datetime.date.today().year)[2:] + '-' + str(random.randint(1000, 9999))


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    details = models.JSONField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=1)

    class Meta:
        abstract = True


class Service(models.Model):
    nom = models.CharField(max_length=225)
    icon = models.CharField(max_length=225, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nom

    @property
    def consultation_count(self):
        return self.consultation_set.count()


class Patient(TimestampedModel):
    situation_matrimoniales_choices = [
        ('Celibataire', 'Celibataire'),
        ('Concubinage', 'Concubinage'),
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
    code_patient = models.CharField(max_length=100, blank=True)
    status = models.PositiveIntegerField(default=0)
    profession = models.CharField(max_length=100, null=True, blank=True)
    nbr_enfants = models.PositiveIntegerField(default=0)
    groupe_sanguin = models.CharField(max_length=20, null=True)
    niveau_etude = models.CharField(max_length=100, null=True, blank=True)
    employeur = models.CharField(max_length=100, null=True, blank=True)

    def save(
            self, *args, **kwargs
    ):
        if self.code_patient == '':
            self.code_patient = get_random_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.prenoms} {self.nom}'

    class Meta:
        ordering = ['-created_at']


class Domicile(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='domiciles')
    pays = models.CharField(max_length=200, null=True, blank=True)
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)
    ville = models.CharField(max_length=100, null=True, blank=True)
    commune = models.CharField(max_length=100, null=True, blank=True)
    quartier = models.CharField(max_length=100, null=True, blank=True)

    @property
    def actuel(self) -> bool:
        return self.date_fin is None


class CategorieMaladies(models.Model):
    nom = models.CharField(max_length=225)


class Maladie(models.Model):
    nom= models.CharField(max_length=225)
    slug = models.CharField(max_length=225, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    code = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nom


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
    charge_viral = models.JSONField(null=True, blank=True)
    bilan_biologique = models.JSONField(null=True, blank=True)


    class Meta:
        ordering = ['-created_at']


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
    pression_arterielle = models.FloatField(default=0)
    frequence_respiratoire = models.FloatField(default=0)
    saturation_oxygene = models.FloatField(default=0)

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
    motif = models.TextField(null=True, blank=True)
    state = models.PositiveIntegerField(default=0)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)


class UniteHospitalisation(models.Model):
    nom = models.CharField(max_length=100)
    capacite = models.PositiveIntegerField(default=1)
    type = models.CharField(max_length=100)

    def __str__(self): return self.nom


class ChambreHospitalisation(models.Model):
    unite = models.ForeignKey(UniteHospitalisation, on_delete=models.CASCADE, related_name='chambres')
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class BoxHospitalisation(models.Model):
    chambre = models.ForeignKey(ChambreHospitalisation, on_delete=models.CASCADE, related_name='boxes')
    capacite = models.PositiveIntegerField(default=1)
    nom = models.CharField(max_length=100)
    occuper = models.BooleanField(default=False)


class Hospitalisation(TimestampedModel):
    state = models.PositiveIntegerField(default=0)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    unite = models.ForeignKey(BoxHospitalisation, on_delete=models.CASCADE)


class Urgence(TimestampedModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='urgences')
    state = models.PositiveIntegerField(default=0)


class Status(TimestampedModel):
    nom = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self): return self.nom


@receiver(models.signals.post_save, sender=Hospitalisation)
def on_hospitalisation_save(sender, instance, created, **kwargs):
    if instance.unite is not None:
        box = instance.unite
        box.occuper = True
        box.save()