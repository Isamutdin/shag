from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import *


# Register your models here.

class PostAdminForm(forms.ModelForm):
    note = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Question
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

admin.site.register(TestQuestions_m2m)
admin.site.register(TypeAnswer)
admin.site.register(Test)
admin.site.register(Question, PostAdmin)