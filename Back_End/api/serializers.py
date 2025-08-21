from rest_framework import serializers  #Transforma a tabela em JSON
from .models import Autor, Editora, Livro

#Serializer utilizado para gerar o dicionário JSON
class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__' #Pega todos os campos torna JSON, para o Python entender

#Serializer utilizado para gerar o dicionário JSON da Editoria
class EditoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'  

#Serializer utilizado para gerar o dicionário JSON da Livro
class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'