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
    type = models.ForeignKey(TypeProduits, on_delete=models.CASCADE)
    categorie = models.ForeignKey(CategoryProduits, on_delete=models.CASCADE)
    reference = models.CharField(max_length=200)
    stock = models.PositiveIntegerField(default=0)
    prix = models.PositiveIntegerField(null=True)


class Ordonance(core_models.TimestampedModel):
    consultation = models.ForeignKey(core_models.Consultation, on_delete=models.CASCADE)

    @property
    def nombre_produit(self)->int:
        return self.lignes.count()

    @property
    def prix_total(self)-> int:
        return 0

class LigneOrdonance(core_models.TimestampedModel):
    ordonance = models.ForeignKey(Ordonance, on_delete=models.CASCADE, related_name='lignes')
    produit = models.ForeignKey(Produit, on_delete=models.SET_NULL, null=True)
    quantite = models.PositiveIntegerField(default=1)
    regle = models.BooleanField(default=False)

    @property
    def prix(self) -> int:
        return self.produit.prix * self.quantite


