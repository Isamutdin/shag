from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('sign_in/', LoginUser.as_view(), name='sign_in'),
    path('sign_up/', RegisterUser.as_view(), name='sign_up'),
    path('logout/', LogoutView.as_view(next_page='sign_in'), name='logout'),

]
