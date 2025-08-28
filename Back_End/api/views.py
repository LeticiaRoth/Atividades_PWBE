from django.shortcuts import render #Renderiza
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

#Importação do Serializer e Autor
from .models import Autor, Editora, Livro
from .serializers import AutorSerializer, EditoraSerializer,LivroSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
#Serve como um post, e o list como get
class AutoresView(ListCreateAPIView):
    #query é um tipo de busca
    #set envia
    queryset = Autor.objects.all() #Aquilo que o usuário verá, no caso todos os objetos dentro da classe Autor
    serializer_class = AutorSerializer
    permission_classes = [IsAuthenticated]
class AutoresCrud(RetrieveUpdateDestroyAPIView): #Realize o método do CRUD dentro da API 
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer #Quando buscados vem em forma de JSON
    permission_classes = [IsAuthenticated]
    filters_backend = [DjangoFilterBackend, SearchFilter]
    filterset_fiel = ['id']
    search_fields = ['nome']
 

#Método do CRUD dos autores
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def visualizacao_autor(request):
    if request.method == 'GET':
        queryset = Autor.objects.all()
        serializer = AutorSerializer(queryset, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AutorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        

#Método para GET, PUT e DELETE       
@api_view(['GET', 'PUT', 'DELETE'])
def detalhes_autores(request,pk):
 
    autor = Autor.objects.get(pk=pk)
   
    if request.method == 'GET':
        serializer = AutorSerializer(autor)
        return Response(serializer.data)
   
    elif request.method == 'PUT':
        serializer = AutorSerializer(autor, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)
       
    elif request.method == 'DELETE':
        autor.delete()
        if serializer.is_valid():
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        




class EditoraView(ListCreateAPIView):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer #Quando buscados vem em forma de JSON
    permission_classes = [IsAuthenticated]
class EditoraCrud(RetrieveUpdateDestroyAPIView):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
    permission_classes = [IsAuthenticated]

#Método do CRUD dos editora
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def visualizar_editora(request):
    if request.method == 'GET':
        queryset = Editora.objects.all()
        serializer = EditoraSerializer(queryset, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EditoraSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)
       

#Método para GET, PUT e DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def detalhes_editoras(request,pk):
 
    editora = Editora.objects.get(pk=pk)
   
    if request.method == 'GET':
        serializer = EditoraSerializer(editora)
        return Response(serializer.data)
   
    elif request.method == 'PUT':
        serializer = EditoraSerializer(editora, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)
       
    elif request.method == 'DELETE':
        editora.delete()
        if serializer.is_valid():
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)



class LivroView(ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer #Quando buscados vem em forma de JSON
    permission_classes = [IsAuthenticated]

class LivroCrud(RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    permission_classes = [IsAuthenticated]

#Método do CRUD dos autores
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def visualizacao_livro(request):
    if request.method == 'GET':
        queryset = Livro.objects.all()
        serializer = LivroSerializer(queryset, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LivroSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)
       
#Método para GET, PUT e DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def detalhes_livros(request,pk):
 
    livro = Livro.objects.get(pk=pk)
   
    if request.method == 'GET':
        serializer = LivroSerializer(livro)
        return Response(serializer.data)
   
    elif request.method == 'PUT':
        serializer = LivroSerializer(livro, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)
       
    elif request.method == 'DELETE':
        livro.delete()
        if serializer.is_valid():
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)