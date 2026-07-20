from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Evento, Ingresso

def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/lista.html', {'eventos': eventos})

def detalhes_evento(request, evento_id):
    evento = Evento.objects.get(id=evento_id)
    return render(request, 'eventos/detalhes_evento.html', {'evento': evento})

def comprar_ingresso(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if evento.estoque > 0:
        evento.estoque -= 1
        evento.save()

        ingresso = Ingresso(evento=evento, comprador=request.user)
        ingresso.save()
        
        return HttpResponse("Ingresso comprado com sucesso!")