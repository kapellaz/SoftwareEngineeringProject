"""formularios para renderizar no html e receber input do user"""

from django import forms


# from .models import Comment, CommentOption


class ReviewForm(forms.Form):
    """ndsnksn"""
    comentarioop1 = forms.CharField(
        label='',
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "new class name two",
                "rows": 2,
                "cols": 30,
                "placeholder": "Introduza o comentário à opção 1",
            }
        )
    )
    comentarioop2 = forms.CharField(
        label='',
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "new class name two",
                "rows": 2,
                "cols": 30,
                "placeholder": "Introduza o comentário à opção 2"
            }
        )
    )
    comentarioop3 = forms.CharField(
        label='',
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "new class name two",
                "rows": 2,
                "cols": 30,
                "placeholder": "Introduza o comentário à opção 3"
            }
        )
    )
    comentarioop4 = forms.CharField(
        label='',
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "new class name two",
                "rows": 2,
                "cols": 30,
                "placeholder": "Introduza o comentário à opção 4"
            }
        )
    )
    comentarioop5 = forms.CharField(
        label='',
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "new class name two",
                "rows": 2,
                "cols": 30,
                "placeholder": "Introduza o comentário à opção 5"
            }
        )
    )
    comentarioop6 = forms.CharField(
        label='',
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "new class name two",
                "rows": 2,
                "cols": 30,
                "placeholder": "Introduza o comentário à opção 6"
            }
        )
    )
    comentario = forms.CharField(
        label='',
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": "new class name two",
                "rows": 10,
                "cols": 30,
                "placeholder": "Introduza o comentário GERAL"
            }
        )
    )
    aprovado = forms.BooleanField(
        required=False
    )

    def clean_comentario(self):
        """trata de um comentario para guardar o texto"""
        if self.is_valid():
            cleaned_data = self.cleaned_data
            comentario = cleaned_data.get('comentario')
            return comentario
        return None
