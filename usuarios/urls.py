from importlib.resources import path
from django.urls import path

from . import views # manipula qual url queremos devolver e exibir ao usuário

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro', views.cadastro, name='cadastro')
]