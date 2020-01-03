from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apiVektorel.models import Music
from apiVektorel.serializers import MusicSerializer

class MusicList(APIView):
    def get(self,request,format=None):
        musics = Music.objects.all()
        serializer = MusicSerializer(musics,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
