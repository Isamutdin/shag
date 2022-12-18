from django import forms
from .models import Question, TypeAnswer, Test
from ckeditor.widgets import CKEditorWidget



class QuestionForm(forms.ModelForm):
    note = forms.CharField(widget=CKEditorWidget())

    answer_type = forms.ModelChoiceField(
        queryset=TypeAnswer.objects.all(),
        empty_label='Тип вопроса',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Question
        exclude = []
        widgets = {
            'score': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Баллы'}),    
        }



class TestForm(forms.ModelForm):
    note = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Test
        exclude = []
        fields = '__all__'
