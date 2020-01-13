from django.urls import path

from .views import ListKayit,DetayKayit

urlpatterns = [
    path('',ListKayit.as_view()),
    path('<int:pk>/',DetayKayit.as_view())

]