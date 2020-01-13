from rest_framework import serializers
from Kayit import models

class KayitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.KayitModel

        fields = (
            "id",
            "adi",
            "soyadi",
            "tcKimlikNo",
        )