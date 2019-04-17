from django import forms
from .models import Pessoa

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