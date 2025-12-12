from django.db import models
from django import forms


# --- Definição das opções (CHOICES) ---
ASSUNTO_CHOICES = (
    ('suporte', 'Suporte técnico'),
    ('comercial', 'Comercial'),
    ('reclamacao', 'Reclamação'),
    ('parceria', 'Parceria'),
    ('financeiro', 'Financeiro'),
)

class ContatoForm(forms.Form):
    
    nome = forms.CharField(
        max_length=100, 
        label='Nome Completo',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'})
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'})
    )

    
    telefone = forms.CharField(
        max_length=15, 
        label='Telefone / WhatsApp',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(99) 99999-9999'}) #
    )

    
    assunto = forms.ChoiceField(
        choices=ASSUNTO_CHOICES, 
        label='Assunto do Contato',
        widget=forms.Select(attrs={'class': 'form-control'}) 
    )

    mensagem = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escreva sua mensagem', 'rows': 4})
    )


class ProdutoForm(forms.Form):
    nome = forms.CharField(
        max_length=100,
        label='Nome do Produto',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Impressora'})
    )

    preco = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label='Preço',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 600.00'})
    )

    estoque = forms.IntegerField(
        label='Estoque',
        min_value=0, # Opcional: Garante que o estoque não é negativo
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 10'})
    )