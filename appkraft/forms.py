from django import forms
from .models import *

class ProdutosModelForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = [
            'nome',
            'empresa',
            'custo',
            'ganho',
            'valor',
            'estoque_atual',
            'estoque_minimo',
            'observacoes',
            'foto',
        ]

        widgets={
            'observacoes':forms.Textarea(attrs={'placeholder':'Até 255 caracteres..','rows':3}),
            'nome':forms.TextInput(attrs={'placeholder':'Nome Produto'}),
        }