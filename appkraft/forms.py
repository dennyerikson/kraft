from django import forms
from .models import *

class ProdutosModelForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = [
            'codigo_produto',
            'codigo_barras',
            'nome',
            'descricao',
            'empresa',
            'custo',
            'ganho',
            'valor',
            'marca',
            'estoque_atual',
            'estoque_minimo',
            'observacoes',
            'foto',
        ]

        widgets={
            'observacoes':forms.Textarea(attrs={'placeholder':'Até 255 caracteres..','rows':3}),
            'nome':forms.TextInput(attrs={'placeholder':'Nome Produto'}),
        }