from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.cadastro, name='registrar'),
]