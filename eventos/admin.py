from django.contrib import admin

from eventos.models import Evento, Comprador, Ingresso

admin.site.register(Evento)
admin.site.register(Comprador)
admin.site.register(Ingresso)