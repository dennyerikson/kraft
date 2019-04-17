from django import forms
from .models import Pessoa
from django.contrib.admin import widgets


class PessoaModelForm(forms.ModelForm):
    class Meta :
        model = Pessoa
        fields = [
            'perfil',
            'cpf',
            'nome',
            'aniverssario',
            'contato',
            'endereco',
            'cnpj',
            'n_ie',
            'n_im',
            'foto',
        ]

        widgets = {
            'aniverssario':forms.DateInput(attrs={'class':"datetime-input"}),
            'endereco':forms.TextInput(attrs={
                'name':'cep', 'type':'text', 'id':'cep', 'value':'', 'onblur':'pesquisacep(this.value)'
                })
        }