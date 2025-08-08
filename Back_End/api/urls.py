from django.urls import path
from .views import *

#Crio os endpoints
urlpatterns = [
    path('autores', AutoresView.as_view()) ,#URLS para CRUD no banco de dados
    path('crud/<int:pk>/', AutoresCrud.as_view())
]

