from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:evento_id>/", views.detalhe_evento, name="detalhe_evento"),
    path("<int:evento_id>/comprar/", views.comprar_ingresso, name="comprar_ingresso")
]