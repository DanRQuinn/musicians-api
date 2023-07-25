from rest_framework import serializers
from .models import Musician

class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner', 'name', 'instrument', 'created_at', 'updated_at')
        model = Musician


