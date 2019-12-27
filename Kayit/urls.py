from django.urls import path,include
from . import views



urlpatterns = [
    path('liste/',views.kayitliste,name="kayitliste"),
    path('detay/<int:pk>',views.kayitdetay,name="kayitdetay"),
]
