from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        senhaConfirmada = request.POST['senhaConfirmada']
        if not nome.strip():
            print('o nome não pode ficar em branco')
            return redirect('cadastro')
        if not email.strip():
            print('o email não pode ficar em branco')
            return redirect('cadastro')
        if senha != senhaConfirmada:
            print('as senhas não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print('usuário já cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        print('usuário cadastrado')

        return redirect('index')
    else:
        return render(request, 'usuarios/cadastro.html')


def index(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == "":
            print('os campos de email e senha não podem estar vazios')
            return redirect('index')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                if request.user.is_authenticated:
                    return redirect('home')
                else:
                    return redirect('usuarios/index.html')
    return render(request, 'usuarios/index.html')
