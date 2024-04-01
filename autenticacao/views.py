from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.messages import constants

def welcome(request):
    return render(request, 'welcome.html')

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get('confirmar_senha')

        users = User.objects.filter(username=username)

        if users.exists():
            messages.add_message(request, constants.ERROR, 'Usuário já existe.')
            return redirect('/autenticacao/cadastro')

        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem.')
            return redirect('/autenticacao/cadastro')

        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'A senha deve possuir pelo menos 6 caracteres.')
            return redirect('/autenticacao/cadastro')
        
        try:
            User.objects.create_user(
                username=username,
                email=email,
                password=senha
            )
            messages.add_message(request, constants.ERROR, 'Usuário cadastrado com sucesso.')
            return redirect('/autenticacao/login')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/autenticacao/cadastro')


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get("senha")

        user = auth.authenticate(request, username=username, password=senha)

        if user:
            auth.login(request, user)
            return redirect('/pacientes/home')

        messages.add_message(request, constants.ERROR, 'Usuário ou senha incorretos')
        return redirect('/autenticacao/login')
    
def sair(request):
    auth.logout(request)
    return redirect('/autenticacao/login')