from django.urls import path

from . import views

urlpatterns = [
    path("eventos/listar", views.listar_eventos, name="listar_eventos"),
    path("eventos/<int:evento_id>/", views.detalhes_evento, name="detalhes_evento"),
    path("eventos/<int:evento_id>/comprar/", views.comprar_ingresso, name="comprar_ingresso")
]