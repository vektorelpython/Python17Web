from rest_framework import serializers

from .models import Music

class MusicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=120)

    def create(self,validated_data):
        return Music.objects.create(**validated_data)