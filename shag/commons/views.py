from django.views.generic import CreateView
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from users.forms import CustomUserCreationForm


def blog_home(request):
    return render(request, 'commons/_base.html')
    


class RegisterUser(CreateView):
    form_class = CustomUserCreationForm #модель формы forms.py
    template_name = './commons/auth/register.html'
    success_url = '/home'


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = './commons/auth/login.html'

    def get_success_url(self):
        return reverse_lazy('home')   #переадресация





# python manage.py shell
#Author.object.all() - все авторы
#Topic.objects.all() - все топики
#Topic.objects.filter(author=???) - фильтр по автору
# где ??? - это запрос всех авторов + индекс автора
#Topic.objects.filter(author=   Author.objects.all()[1]    )

