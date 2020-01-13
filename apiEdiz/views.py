from rest_framework import generics
from Kayit import models
from .serializers import KayitSerializer


class ListKayit(generics.ListCreateAPIView):
    queryset = models.KayitModel.objects.all()
    serializer_class = KayitSerializer

class DetayKayit(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.KayitModel.objects.all()
    serializer_class = KayitSerializer

