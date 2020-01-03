from django.shortcuts import render,get_object_or_404,redirect
from .models import KayitModel
from .forms import KayitForm


def kayitliste(request):
    kayits =  KayitModel.objects.all()
    return render(request,"kayit/liste.html",{"kayitlar":kayits})

def kayitdetay(request,pk):
    kayit = get_object_or_404(KayitModel,pk=pk)
    return render(request,"kayit/detay.html",{"kayit":kayit})

def yenikayit(request):
    if request.method == "POST":
        form = KayitForm(request.POST)
        if form.is_valid():
            kayit = form.save(commit=False)
            kayit.kayit_eden = request.user
            kayit.save()
            return redirect('kayitOK')
    else:
        form = KayitForm()
    return render(request,"kayit/yenikayit.html",{"form":form})


def kayitDuzenle(request,pk):
    kayit = get_object_or_404(KayitModel,pk=pk)
    if request.method == "POST":
        form = KayitForm(request.POST,instance=kayit)
        if form.is_valid():
            kayit = form.save(commit=False)
            kayit.kayit_eden = request.user
            kayit.save()
            return redirect('kayitOK')
    else:
        form = KayitForm(instance=kayit)
    return render(request,"kayit/yenikayit.html",{"form":form})