from django.shortcuts import render #Renderiza
from rest_framework.generics import ListCreateAPIView
from .models import Autor
from .serializers import AutorSerializer

#Serve como um post, e o list como get
class AutoresView(ListCreateAPIView):
    #query é um tipo de busca
    #set envia
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
