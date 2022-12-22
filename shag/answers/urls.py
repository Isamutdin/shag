from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('input_create/<int:pk>/', InputAnswerCreateView.as_view(), name='input_create'),
    path('input_update/<int:pk>/<int:id>/', InputAnswerUpdateView.as_view(), name='input_update'),
    path('input_delete/<int:pk>/<int:id>/', InputAnswerDeleteView.as_view(), name='input_delete'),

]