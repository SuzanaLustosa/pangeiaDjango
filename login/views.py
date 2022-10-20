from django.shortcuts import get_object_or_404, render, get_list_or_404
from .models import Aulas

def home(request):
    aulas = Aulas.objects.filter(publicado=True)

    dados = {
        'aulas': aulas
    }

    return render(request, 'home.html', dados)

def perfil(request):
    return render(request, 'perfil.html')

def spanish(request, aula_id):
    aula = get_object_or_404(Aulas, pk=aula_id)

    aula_a_exibir = {
        'aula' : aula
    }

    return render(request, 'spanish.html', aula_a_exibir)

def buscar(request):
    lista_aulas = aulas = Aulas.objects.filter(publicado=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            lista_aulas = lista_aulas.filter(nome_aula__icontains=nome_a_buscar)
    
    dados = {
        'aulas': lista_aulas
    }

    return render(request, 'buscar.html', dados)