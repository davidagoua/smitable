from rest_framework import serializers
from personel import models


class GardUnite(serializers.ModelSerializer):

    class Meta:
        model = models.GardeUnite
        fields = '__all__'


class GardeTour(serializers.ModelSerializer):
    personels = serializers.StringRelatedField(many=True)
    unite = serializers.StringRelatedField()
    class Meta:
        model = models.GardeTour
        fields = '__all__'