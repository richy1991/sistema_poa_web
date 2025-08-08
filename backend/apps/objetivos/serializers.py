from rest_framework import serializers
from .models import ObjetivoEspecifico

class ObjetivoEspecificoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjetivoEspecifico
        fields = '__all__'
