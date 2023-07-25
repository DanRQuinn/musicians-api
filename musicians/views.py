from rest_framework import generics
from .serializer import MusicianSerializer
from .models import Musician

class MusicianList(generics.ListCreateAPIView):
    serializer_class = MusicianSerializer
    queryset = Musician.objects.all()

class MusicianDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MusicianSerializer
    queryset = Musician.objects.all()
