from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import CadastroForm

def cadastro_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('login')
    else:
        form = CadastroForm()

    context = {'form': form}

    return render(request, 'contas/cadastro.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    
    context = {'form': form}
    return render(request, 'contas/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')