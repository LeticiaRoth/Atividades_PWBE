from rest_framework import serializers  #Transforma a tabela em JSON
from .models import Autor

#Serializer utilizado para gerar o dicionário JSON
class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__' #Pega todos os campos torna JSON, para o Python entender
