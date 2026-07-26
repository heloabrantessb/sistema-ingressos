from django.contrib.auth.decorators import login_required
from django.db.models import Min
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Evento, Ingresso, TipoIngresso

def home(request):
    return redirect('index')

def index(request):
    if request.user.is_staff:
        eventos = Evento.objects.order_by('data_evento')
    else:
        eventos = Evento.objects.order_by('data_evento').filter(status='publicado')
        
    return render(request, 'eventos/index.html', {'eventos': eventos})

def detalhe_evento(request, evento_id):
    evento = Evento.objects.get(id=evento_id)
    tipo_ingressos = TipoIngresso.objects.filter(evento=evento)
    context = {    
        'evento': evento,
        'tipos_ingresso': tipo_ingressos,
    }
    return render(request, 'eventos/detalhes_evento.html', context)

# @login_required
# def iniciar_compra(request, evento_id):
#     #se houver escolha de tipo de ingresso
#         #verificar se está tudo certo
#         #mandar para a página de 