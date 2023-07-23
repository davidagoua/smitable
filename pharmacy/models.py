from django.db import models
from core import models as core_models


class CategoryProduits(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
        return self.nom


class TypeProduits(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=200)
    famille = models.CharField(max_length=200, null=True, blank=True)
    denomination = models.CharField(max_length=200, null=True, blank=True)
    conditionnement = models.CharField(max_length=200, null=True, blank=True)
    type = models.ForeignKey(TypeProduits, on_delete=models.CASCADE)
    categorie = models.ForeignKey(CategoryProduits, on_delete=models.CASCADE)
    reference = models.CharField(max_length=200)
    stock = models.PositiveIntegerField(default=0)
    prix = models.PositiveIntegerField(null=True)


class Ordonance(core_models.TimestampedModel):
    consultation = models.ForeignKey(core_models.Consultation, on_delete=models.CASCADE)

    @property
    def nombre_produit(self) -> int:
        return self.lignes.count()

    @property
    def prix_total(self) -> int:
        return 0


class LigneOrdonance(core_models.TimestampedModel):
    ordonance = models.ForeignKey(Ordonance, on_delete=models.CASCADE, related_name='lignes')
    produit = models.ForeignKey(Produit, on_delete=models.SET_NULL, null=True)
    quantite = models.PositiveIntegerField(default=1)
    regle = models.BooleanField(default=False)

    @property
    def prix(self) -> int:
        return self.produit.prix * self.quantite


class Protocol(core_models.TimestampedModel):
    patient = models.ForeignKey(core_models.Patient, on_delete=models.CASCADE)
    nom = models.CharField(max_length=200, null=True, blank=True)
    duree_month = models.PositiveIntegerField(default=1)
    data = models.JSONField(null=True, blank=True)
    molecules = models.ManyToManyField('Molecule', related_name='protocols', null=True)
    commentaire = models.TextField(null=True, blank=True)
    canceled = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'protocole {self.nom}'


class CategorieMolecule(models.Model):
    nom = models.CharField(max_length=200)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.nom

class Molecule(models.Model):
    nom = models.CharField(max_length=200)
    medicaments = models.ManyToManyField('Produit', related_name='molecules', null=True, blank=True)
    categorie = models.ForeignKey(CategorieMolecule, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nom