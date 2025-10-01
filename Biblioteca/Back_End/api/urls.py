from django.urls import path
from .views import *
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API Livraria",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("Autores/", views.listar_autores, name='listar-autores'),
    path("Autores/<int:pk>/", views.detalhes_autores, name='detalhes-autores'),
    
    path("Editoras/", views.listar_editoras, name='listar-editoras'),
    path("Editoras/<int:pk>/", views.detalhes_editoras, name='detalhes-editoras'),

    path("Livros/", views.listar_livros, name='listar-livros'),
    path("Livros/<int:pk>/", views.detalhes_livros, name='detalhes-livros'),

    # Token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    
]

