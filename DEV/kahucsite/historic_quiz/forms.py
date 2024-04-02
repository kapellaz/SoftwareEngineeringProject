from django import forms
from django.core.exceptions import ValidationError



CHOICES = (
    (True, "V"),
    (False, "F")
)

TAGS = (
    (1, "PM  (Gestão de projecto)"),
    (2, "REQ (requisitos)"),
    (3, "A&D (Arquitectura e design)"),
    (4, "IMP (Implementação)"),
    (5, "TST (testes e qualidade de produto)"),
    (6, "V&V (Verification and Validation)"),
    (7, "DEP (deployment)"),
    (8, "CI  (Continuous practices)"),
    (9, "PRC (boas-práticas e qualidade de Processos)"),
    (10, "PPL (Peopleware)"),
    (11, "CCM (Configuration and Change Management)"),
    (12, "RSK (Risk management)")
)


class EditQuizzForms(forms.Form):
    """A class with fields of a quizz."""

    question = forms.CharField(max_length=200)
    description = forms.CharField(max_length=512, required=False)

    option1 = forms.CharField(max_length=200)
    description1 = forms.CharField(max_length=512)
    field1 = forms.TypedChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    option2 = forms.CharField(max_length=200)
    description2 = forms.CharField(max_length=512)
    field2 = forms.TypedChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    option3 = forms.CharField(max_length=200)
    description3 = forms.CharField(max_length=512)
    field3 = forms.TypedChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    option4 = forms.CharField(max_length=200)
    description4 = forms.CharField(max_length=512)
    field4 = forms.TypedChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    option5 = forms.CharField(max_length=200)
    description5 = forms.CharField(max_length=512)
    field5 = forms.TypedChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    option6 = forms.CharField(max_length=200)
    description6 = forms.CharField(max_length=512)
    field6 = forms.TypedChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    tag = forms.ChoiceField(choices=TAGS, required=False,
                            widget=forms.RadioSelect)

    def clean(self):
        """Verify if only one field is True."""
        cleaned_data = super().clean()
        count = 0
        aa = self.cleaned_data['field1']
        if aa == 'True':
            count += 1
        if self.cleaned_data['field2'] == 'True':
            count += 1
        if self.cleaned_data['field3'] == 'True':
            count += 1
        if self.cleaned_data['field4'] == 'True':
            count += 1
        if self.cleaned_data['field5'] == 'True':
            count += 1
        if self.cleaned_data['field6'] == 'True':
            count += 1
        if count != 1:
            raise ValidationError("✖ Só uma opcao pode ser verdadeira!")


