from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('signup/', RegisterUser.as_view(), name='sign_up'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

]
