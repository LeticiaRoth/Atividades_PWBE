from rest_framework import serializers  #Transforma a tabela em JSON
from .models import Autor

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__' #Pega todos os campos
