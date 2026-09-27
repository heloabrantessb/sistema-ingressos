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

@login_required
def iniciar_compra(request, evento_id):
    """
        if houver escolha de tipo de ingresso
            verificar se todas as constraints estão válidas
            mandar para a página de criar_pedido
            verificar se o usuário atual já possui o maximo de ingressos
            por categoria ao considerar sessoes de compra anteriores

            se todas as validações passarem
                diminui o estoque em 1
                cria pedido com status "PENDENTE"e valor total
                redirecionar para página de pagamento
        
        else 
            exibir alerta "Selecione um tipo de ingresso" 
    """
    evento = get_object_or_404(Evento, id=evento_id)
    tipos_ingresso = TipoIngresso.objects.filter(evento=evento)
    
    for tipo in tipos_ingresso:
        quantidade = request.POST.get(f'ingressos[{tipo.id}]', 0)

    if reques.method == 'POST':
        
        ingressos_pedidos = request.POST.getlist('ingressos')

        if ingressos_pedidos:
            print("logica")

    
    
        
