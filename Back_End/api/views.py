from django.shortcuts import render #Renderiza
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Autor
from .serializers import AutorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#Serve como um post, e o list como get
class AutoresView(ListCreateAPIView):
    #query é um tipo de busca
    #set envia
    queryset = Autor.objects.all() #Aquilo que o usuário verá, no caso todos os objetos dentro da classe Autor
    serializer_class = AutorSerializer

class AutoresCrud(RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

@api_view(["GET", "PUSH"])
def visualizacao_autor(request):
    if request.method == "GET": 
        queryset = Autor.objects.all()
        serializer = AutorSerializer(queryset, many = True)
        return (serializer.data)
    elif request.method == "POST":
        serializer = AutorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)