from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Min, Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Evento, Ingresso, TipoIngresso, Comprador, Pedido, ItemPedido

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
    evento = get_object_or_404(Evento, id=evento_id)
    
    if request.method == 'POST':
        tipos_ingresso = TipoIngresso.objects.filter(evento=evento, ativo=True)
        
        comprador, _ = Comprador.objects.get_or_create(user=request.user)
        
        itens_para_processar = []
        valor_total_pedido = 0
        total_ingressos_selecionados = 0

        for tipo in tipos_ingresso:
            qtd_ingresso = request.POST.get(f'ingressos[{tipo.id}]', '0')
            try:
                qtd = int(qtd_str)
            except ValueError:
                qtd = 0

            if qtd > 0:
                if qtd > tipo.estoque:
                    messages.error(request, f"Estoque insuficiente para o ingresso '{tipo.nome}'. Restantes: {tipo.estoque}.")
                    return redirect('detalhe_evento', evento_id=evento.id)

                total_ingressos_selecionados += qtd
                valor_subtotal = tipo.preco * qtd
                valor_total_pedido += valor_subtotal
                itens_para_processar.append((tipo, qtd))

        if total_ingressos_selecionados == 0:
            messages.warning(request, "Selecione um tipo de ingresso")
            return redirect('detalhe_evento', evento_id=evento.id)

        with transaction.atomic():
            pedido = Pedido.objects.create(
                comprador=comprador,
                evento=evento,
                status=Pedido.Status.PENDENTE,
                valor_total=valor_total_pedido
            )

            for tipo, qtd in itens_para_processar:
                tipo.estoque -= qtd
                tipo.save()

                ItemPedido.objects.create(
                    pedido=pedido,
                    tipo_ingresso=tipo,
                    quantidade=qtd,
                    preco_unitario=tipo.preco
                )

                for _ in range(qtd):
                    Ingresso.objects.create(
                        pedido=pedido,
                        tipo_ingresso=tipo
                    )

        messages.success(request, f"Pedido #{pedido.id} iniciado com sucesso!")
        return redirect('detalhe_evento', evento_id=evento.id)

    return redirect('detalhe_evento', evento_id=evento.id)
