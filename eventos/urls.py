from django.urls import path

from . import views

urlpatterns = [
    path("", views.listar_eventos, name="listar_eventos"),
    path("eventos/<int:evento_id>/", views.detalhes_evento, name="detalhes_evento")
]