from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from .views import *

urlpatterns = [
    path('question_create/<int:pk>/', QuestionCreateView.as_view(), name='question_create'),#pk теста
    path('question_update/<int:pk>/<int:id>/', QuestionUpdateView.as_view(), name='question_update'),#pk вопроса, а id теста
    path('question_delete/<int:pk>/<int:id>/', QuestionDeleteView.as_view(), name='question_delete'),

    path('test_create/', TestCreateView.as_view(), name='test_create'),
]
