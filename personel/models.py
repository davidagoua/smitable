from django.db import models
from core import models as core_models



class GardeUnite(models.Model):
    nom = models.CharField(max_length=100)

class GardeTour(core_models.TimestampedModel):
    date_debut = models.DateField()
    date_fin = models.DateField()
    actif = models.BooleanField(default=True)
    personels = models.ManyToManyField(core_models.User, related_name='gardes')
    unite = models.ForeignKey(GardeUnite, on_delete=models.CASCADE, null=True)
