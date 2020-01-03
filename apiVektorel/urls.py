from django.urls import path

from apiVektorel.views import MusicList

urlpatterns = [
    path('musics/',MusicList.as_view()),
]