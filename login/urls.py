from importlib.resources import path
from django.urls import path

from . import views # manipula qual url queremos devolver e exibir ao usuário

urlpatterns = [
    path('home', views.home, name='home'),
    path('perfil', views.perfil, name='perfil'),
    path('<int:aula_id>', views.spanish, name='spanish'),
    path('busca', views.buscar, name='buscar')
]