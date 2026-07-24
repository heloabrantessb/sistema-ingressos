from django.contrib import admin

from eventos.models import Evento, TipoIngresso, Comprador, Pedido, Ingresso

class TipoIngressoInline(admin.StackedInline):
    model = TipoIngresso
    extra = 0

class EventoAdmin(admin.ModelAdmin):
    inlines = [TipoIngressoInline]
    # list_display = ('nome', 'data', 'local', 'status')
    # list_filter = ('data', 'status')
    # search_fields = ('nome', 'local')
    # ordering = ('data',)
    
admin.site.register(Evento, EventoAdmin)
admin.site.register(TipoIngresso)
admin.site.register(Comprador)
admin.site.register(Pedido)
admin.site.register(Ingresso)