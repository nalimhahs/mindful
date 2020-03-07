from django import forms
from .models import Answer

class AnswerForm(forms.Form):

    answer = forms.ChoiceField(choices=Answer.CHOICES, widget=forms.RadioSelect)
