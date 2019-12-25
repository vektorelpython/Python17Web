from django.shortcuts import render
from .models import KayitModel


def kayitliste(request):
    kayits =  KayitModel.objects.all()
    return render(request,"home.html",{"kayitlar":kayits})