from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
 
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Your API Title",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@yourapi.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


#Crio os endpoints
urlpatterns = [
    path('autores', AutoresView.as_view()) ,#URLS para CRUD no banco de dados
    path('authors', visualizacao_autor ),
    path('editoras', EditoraView.as_view()),
    path('livro', LivroView.as_view()),

    path('autor/<int:pk>', AutoresCrud.as_view()),
    path('editora/<int:pk>', EditoraCrud.as_view()),
    path('livro/<int:pk>', LivroCrud.as_view()),

    #Token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('search/', AutoresView.as_view()),
]