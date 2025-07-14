# PBD beta/apps/itens/forms.py

from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        # Adicione os novos campos ao formulário
        fields = ['nome', 'descricao', 'imagem', 'tipo', 'status', 'quantidade', 'preco_diario', 'empresa']