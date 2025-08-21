from django.urls import path
from .views import *
 
#Crio os endpoints
urlpatterns = [
    path('autores', AutoresView.as_view()) ,#URLS para CRUD no banco de dados
    path('authors', visualizacao_autor ),
    path('editoras', EditoraView.as_view()),
    path('livro', LivroView.as_view()),

    path('autor<int:pk>', AutoresCrud.as_view()),
    path('editora<int:pk>', EditoraCrud.as_view()),
    path('livro<int:pk>', LivroCrud.as_view())
]