from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import *
from .forms import *
# Create your views here.


class InputAnswerCreateView(CreateView):
    model = InputAnswer
    template_name = 'answer/input_form.html'
    form_class = InputAnswerForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['answers'] = InputAnswer.objects.filter(question_id=self.kwargs['pk'])
        return data

    def form_valid(self, form):
        form.cleaned_data['question_id'] = self.kwargs['pk']
        answer = InputAnswer.objects.create(**form.cleaned_data)#создаю в бд вопрос
        answer.save()
        return redirect(self.get_success_url())

    def get_success_url(self) -> str:
        return reverse('input_create', args=[self.kwargs['pk']])



class InputAnswerUpdateView(UpdateView):
    model = InputAnswer
    template_name = 'answer/input_form.html'
    form_class = InputAnswerForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['answers'] = InputAnswer.objects.filter(question_id=self.kwargs['id'])
        return data

    def get_success_url(self) -> str:
        return reverse('input_create', args=[self.kwargs['id']])


class InputAnswerDeleteView(DeleteView):
    model = InputAnswer
    template_name = 'answer/input_confirm_delete.html'

    def get_success_url(self) -> str:#id теста
        return reverse("input_create", args=[self.kwargs['id']])