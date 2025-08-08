from django.shortcuts import render #Renderiza
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Autor
from .serializers import AutorSerializer

#Serve como um post, e o list como get
class AutoresView(ListCreateAPIView):
    #query é um tipo de busca
    #set envia
    queryset = Autor.objects.all() #Aquilo que o usuário verá, no caso todos os objetos dentro da classe Autor
    serializer_class = AutorSerializer

class AutoresCrud(RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
