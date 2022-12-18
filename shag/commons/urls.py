from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', blog_home, name="home"),
]
