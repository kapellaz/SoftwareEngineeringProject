"""formularios para renderizar no html e receber input do user"""

from django import forms


# from .models import Comment, CommentOption


class CreateTestForm(forms.Form):
    title = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "new class name two",
                "cols": 30,
                "placeholder": "Introduza o título"
            }
        )
    )
    tag1 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'tags'}
                                   ))
    tag2 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'tags'}
                                   )
    )
    tag3 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'tags'}
                                   )
    )
    tag4 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'tags'}
                                   )
    )
    tag5 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'tags'}
                                   )
    )
    tag6 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'tags'}
                                   )
    )
    tag7 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'tags'}
                                   )
    )
    tag8 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'tags'}
                                   )
    )
    tag9 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'tags'}
                                   )
    )
    tag10 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'tags'}
                                   )
    )
    tag11 = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'tags'}
                                   )
    )
    tag12 = forms.BooleanField(
        required=False,widget=forms.CheckboxInput(attrs={'class': 'tags'}
                                   )
    )

    def labels(self, all_tags):

        # print(all_tags)

        for i in range(len(all_tags)):
            self.fields["tag" + str(i + 1)].label = all_tags[i]
        return None

    def clean_tittle(self, name):
        """trata de um comentario para guardar o texto"""
        if self.is_valid():
            cleaned_data = self.cleaned_data
            data = cleaned_data.get(name)
            return data
        return None
