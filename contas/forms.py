from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth.models import User
from .models import Comprador

class CadastroForm(UserCreationForm):
    nome_completo = forms.CharField(required=True)
    cpf = forms.CharField(required=True, max_length=14)
    telefone = forms.CharField(max_length=11, required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'nome_completo', 'cpf', 'telefone']

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.nome_completo = self.cleaned_data['nome_completo']
        user.cpf = self.cleaned_data['cpf']
        user.telefone = self.cleaned_data.get('telefone', '')
        
        if commit:
            user.save()
            Comprador.objects.create(
                user=user, 
                nome_completo=user.nome_completo, 
                cpf=user.cpf, 
                telefone=user.telefone)
        return user
    
    