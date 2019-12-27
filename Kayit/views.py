from django.shortcuts import render,get_object_or_404
from .models import KayitModel
from .forms import KayitForm


def kayitliste(request):
    kayits =  KayitModel.objects.all()
    return render(request,"kayit/liste.html",{"kayitlar":kayits})

def kayitdetay(request,pk):
    kayit = get_object_or_404(KayitModel,pk=pk)
    return render(request,"kayit/detay.html",{"kayit":kayit})

def yenikayit(request):
    form = KayitForm()
    return render(request,"kayit/yenikayit.html",{"form":form})