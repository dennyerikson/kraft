from django import forms
from .models import Lista


# form create list
class ListaModelForm(forms.ModelForm):
    class Meta:
        model = Lista
        fields = [
            'lista',
        ]