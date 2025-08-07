from django.urls import path
from .views import *

#Crio os endpoints
urlpatterns = [
    path('autores', AutoresView.as_view())
]

