"""A form to get data from POST request."""
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


class NewQuizz(forms.Form):
    """A class with fields of a quizz."""

    question = forms.CharField(max_length=200)
    description = forms.CharField(max_length=512, required=False)

    answer1 = forms.CharField(max_length=200)
    reason1 = forms.CharField(max_length=512)
    option1 = forms.TypedChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    answer2 = forms.CharField(max_length=200)
    reason2 = forms.CharField(max_length=512)
    option2 = forms.TypedChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    answer3 = forms.CharField(max_length=200)
    reason3 = forms.CharField(max_length=512)
    option3 = forms.TypedChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    answer4 = forms.CharField(max_length=200)
    reason4 = forms.CharField(max_length=512)
    option4 = forms.TypedChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    answer5 = forms.CharField(max_length=200)
    reason5 = forms.CharField(max_length=512)
    option5 = forms.TypedChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    answer6 = forms.CharField(max_length=200)
    reason6 = forms.CharField(max_length=512)
    option6 = forms.TypedChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    tag = forms.ChoiceField(choices=TAGS, required=False,
                            widget=forms.RadioSelect, localize=True)

    def clean(self):
        """Verify if only one field is True."""
        count = 0
        if self.cleaned_data['option1'] == 'True':
            count += 1
        if self.cleaned_data['option2'] == 'True':
            count += 1
        if self.cleaned_data['option3'] == 'True':
            count += 1
        if self.cleaned_data['option4'] == 'True':
            count += 1
        if self.cleaned_data['option5'] == 'True':
            count += 1
        if self.cleaned_data['option6'] == 'True':
            count += 1
        if count != 1:
            raise ValidationError("✖ Só uma opcao pode ser verdadeira!")

        if not self.cleaned_data['tag']:
            raise ValidationError("✖ Adicione uma tag!")
