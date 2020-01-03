from django.urls import path,include
from . import views
from django.views.generic.base import TemplateView



urlpatterns = [
    path('liste/',views.kayitliste,name="kayitliste"),
    path('detay/<int:pk>',views.kayitdetay,name="kayitdetay"),
    path('yenikayit/',views.yenikayit,name="yenikayit"),
    path('kayitOK/',TemplateView.as_view(template_name="kayit/kayitTamam.html"),name="kayitOK"),
    path('kayitDuzenle/<int:pk>',views.kayitDuzenle,name='kayitDuzenle')
]
