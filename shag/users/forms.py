from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms




class CustomUserCreationsFrom(UserCreationForm):
    
    email = forms.CharField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = CustomUser
        exclude = []
        fields = ('username', 'email', 'phone', )



