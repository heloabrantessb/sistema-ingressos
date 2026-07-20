from django.shortcuts import render
from django.http import HttpResponse
from .models import Evento

def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/', {'eventos': eventos})

def detalhes_evento(request, evento_id):
    evento = Evento.objects.get(id=evento_id)
    return render(request, 'eventos/detalhes_evento.html', {'evento': evento})

def comprar_ingresso(request, evento_id):
    evento = Evento.objects.get(id=evento_id)
    