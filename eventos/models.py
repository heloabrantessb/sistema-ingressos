from django.db import models
from django.contrib.auth.models import User
import uuid

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    local = models.CharField(max_length=200)
    data_evento = models.DateTimeField()
    data_fim_vendas = models.DateTimeField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
class TipoIngresso(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField()
    
class Comprador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='comprador')
    nome_completo = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=11, null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nome_completo} - {self.user.username}"

class Pedido(models.Model):
    comprador = models.ForeignKey(Comprador, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[
        ('pendente', 'Pendente'), 
        ('pago', 'Pago'), 
        ('cancelado', 'Cancelado')])
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_criacao = models.DateTimeField(auto_now_add=True)
    pago_em = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Pedido {self.id} - {self.comprador.nome_completo}"

class Ingresso(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    tipo_ingresso = models.ForeignKey(TipoIngresso, on_delete=models.CASCADE)
    codigo_validacao = models.UUIDField(unique=True, default=uuid.uuid4())
    emitido_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ingresso para {self.pedido.evento.titulo} - Comprador: {self.pedido.comprador.nome}"