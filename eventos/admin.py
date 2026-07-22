from django.contrib import admin

from eventos.models import Evento, TipoIngresso, Comprador, Pedido, Ingresso

admin.site.register(Evento)
admin.site.register(TipoIngresso)
admin.site.register(Comprador)
admin.site.register(Pedido)
admin.site.register(Ingresso)