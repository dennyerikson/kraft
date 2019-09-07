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
            'observacoes':forms.Textarea(attrs={
                'placeholder':'Aqui é a descrição do seu produto, destalhes, sabores, marcas e etc...'
                    +'Até 255 caracteres..', 'rows':2}),
            'nome':forms.TextInput(attrs={'placeholder':'Nome Produto'}),
            'custo':forms.TextInput(attrs={'placeholder':'Valor gasto em R$'}),
            'ganho':forms.TextInput(attrs={'placeholder':'Ganho em %', 'disabled':'true'}),
            'valor':forms.TextInput(attrs={'placeholder':'Valor pretendido R$'}),
        }