from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms




class CustomUserCreationsFrom(UserCreationForm):
    
    email = forms.CharField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}))
    
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        exclude = []
        fields = ('username', 'email', 'phone', )

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'phone'})
        }

