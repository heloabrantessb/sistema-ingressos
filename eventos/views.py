from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Evento, Ingresso, TipoIngresso 

def home(request):
    return redirect('index')

def index(request):
    eventos = Evento.objects.all()
    context = {'eventos': eventos}
    return render(request, 'eventos/index.html', context)

def detalhe_evento(request, evento_id):
    evento = Evento.objects.get(id=evento_id)
    tipo_ingressos = TipoIngresso.objects.filter(evento=evento)
    context = {
        'evento': evento,
        'tipos_ingresso': tipo_ingressos
    }
    return render(request, 'eventos/detalhes_evento.html', context)

@login_required
def comprar_ingresso(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if evento.estoque > 0:
        evento.estoque -= 1
        evento.save()

        ingresso = Ingresso(evento=evento, comprador=request.user)
        ingresso.save()
        
        return HttpResponse("Ingresso comprado com sucesso!")