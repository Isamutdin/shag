from django import forms
from .models import Question, Test, QuestionType
from ckeditor.widgets import CKEditorWidget



class QuestionForm(forms.ModelForm):
    note = forms.CharField(widget=CKEditorWidget())

    question_type = forms.ModelChoiceField(
        queryset=QuestionType.objects.all(),
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
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название теста'}),
            'max_score': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Баллы'}),
            'complexity': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Сложность'})
        }