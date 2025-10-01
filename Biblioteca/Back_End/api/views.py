from django.shortcuts import render
from .models import Autor, Livro, Editora
from .serializers import AutorSerializers, LivroSerializers, EditoraSerializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

# ==== View Autores ==== #
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def listar_autores(request):
    if request.method == 'GET':
        filter_backends = [DjangoFilterBackend, SearchFilter]
        queryset = Autor.objects.all()

        for backend in list(filter_backends):
            queryset = backend().filter_queryset(request, queryset, view=listar_autores)

        serializer = AutorSerializers(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AutorSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

listar_autores.filter_backends = [DjangoFilterBackend, SearchFilter]
listar_autores.filterset_fields = ['nacionalidade', 'data_nascimento']
listar_autores.search_fields = ['nome', 'sobrenome']

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
@permission_classes([IsAuthenticated])
def detalhes_autores(request,pk):

    autor = Autor.objects.get(pk=pk)
    
    if request.method == 'GET':
        serializer = AutorSerializers(autor)
        return Response(serializer.data)
    
    elif request.method == 'PUT': 
        serializer = AutorSerializers(autor, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'PATCH': 
        serializer = AutorSerializers(autor, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        autor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# ==== View Autores ==== #

# ==== View Editoras ==== #
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def listar_editoras(request):
    if request.method == 'GET':
        filter_backends = [DjangoFilterBackend, SearchFilter]
        queryset = Editora.objects.all()

        for backend in list(filter_backends):
            queryset = backend().filter_queryset(request, queryset, view=listar_editoras)

        serializer = EditoraSerializers(queryset, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EditoraSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
listar_editoras.filter_backends = [DjangoFilterBackend, SearchFilter]
listar_editoras.filterset_fields = ['cnpj', 'telefone']
listar_editoras.search_fields = ['editora', 'site']

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
# @permission_classes([IsAuthenticated])
def detalhes_editoras(request,pk):

    editora = Editora.objects.get(pk=pk)
    
    if request.method == 'GET':
        serializer = EditoraSerializers(editora)
        return Response(serializer.data)
    
    elif request.method == 'PUT': 
        serializer = EditoraSerializers(editora, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH': 
        serializer = EditoraSerializers(editora, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        editora.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# ==== View Editoras ==== #

# ==== View Livros ==== #
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def listar_livros(request):
    if request.method == 'GET':
        filter_backends = [DjangoFilterBackend, SearchFilter]
        queryset = Livro.objects.all()

        for backend in list(filter_backends):
            queryset = backend().filter_queryset(request, queryset, view=listar_livros)

        serializer = LivroSerializers(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LivroSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
listar_livros.filter_backends = [DjangoFilterBackend, SearchFilter]
listar_livros.filterset_fields = ['titulo', 'subtitulo']
listar_livros.search_fields = ['isbn', 'idioma']

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
@permission_classes([IsAuthenticated])
def detalhes_livros(request,pk):

    livro = Livro.objects.get(pk=pk)
    
    if request.method == 'GET':
        serializer = LivroSerializers(livro)
        return Response(serializer.data)
    
    elif request.method == 'PUT': 
        serializer = LivroSerializers(livro, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = LivroSerializers(livro, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        livro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# ==== View Livros ==== #             