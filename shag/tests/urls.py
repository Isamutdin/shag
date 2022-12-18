from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from .views import *

urlpatterns = [
    path('question_create/<int:pk>/', QuestionCreateView.as_view(), name='question_create'),
    path('test_create/', TestCreateView.as_view(), name='test_create'),
]
