from django.shortcuts import render, redirect
from .forms import CadastroForm

def cadastro(request):
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