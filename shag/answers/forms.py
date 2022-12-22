from django import forms
from .models import *


class InputAnswerForm(forms.ModelForm):

    class Meta:
        model = InputAnswer
        exclude = []
        fields = ('right_answer',)
