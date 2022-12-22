from .forms import *
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView

# Create your views here.

class RegisterUser(CreateView):
    model = CustomUser
    template_name = 'user/register.html'
    form_class = CustomUserCreationsFrom
    
    def get_success_url(self) -> str:
        return reverse('login')


class LoginUser(LoginView):
    model = CustomUser
    template_name = 'user/login.html'

    def get_success_url(self) -> str:
        return reverse('home')