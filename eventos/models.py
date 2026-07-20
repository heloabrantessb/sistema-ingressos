from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_evento = models.DateTimeField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo
    
class Comprador(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.nome

class Ingresso(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    comprador = models.ForeignKey(Comprador, on_delete=models.CASCADE)
    codigo_validacao = models.UUIDField(max_length=100, unique=True)
    comprado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ingresso para {self.evento.titulo} - Comprador: {self.comprador.nome}"