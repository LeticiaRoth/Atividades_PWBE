from rest_framework import serializers
from .models import Autor, Livro, Editora

class AutorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'
        extra_kwargs = {
            'nome': {'required': False},
            'sobrenome': {'required': False},
            'data_nascimento': {'required': False},
            'nacionalidade': {'required': False},
            'biografia': {'required': False},
        }

class EditoraSerializers(serializers.ModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'
        extra_kwargs = {
            'editora': {'required': False},
            'cnpj': {'required': False},
            'endereco': {'required': False},
            'telefone': {'required': False},
            'email': {'required': False},
            'site': {'required': False}
        }


class LivroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'
        extra_kwargs = {
            'titulo': {'required': False},
            'subtitulo': {'required': False},
            'autor': {'required': False},
            'editor': {'required': False},
            'isbn': {'required': False},
            'descricao': {'required': False},
            'idioma': {'required': False},
            'ano_publicacao': {'required': False},
            'paginas': {'required': False},
            'preco': {'required': False},
            'estoque': {'required': False},
            'desconto': {'required': False},
            'disponivel': {'required': False},
            'dimensoes': {'required': False},
            'peso': {'required': False},
        }