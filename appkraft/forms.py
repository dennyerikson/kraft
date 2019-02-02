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
            'valor',
            'marca',
            'estoque_atual',
            'estoque_minimo',
            'observacoes',
            'foto',
        ]