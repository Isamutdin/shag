from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Question, Test, TestQuestions_m2m
from .forms import QuestionForm, TestForm

# Create your views here.


class QuestionCreateView(CreateView):
    model = Question
    template_name = "question/question_form.html"
    form_class = QuestionForm

    def get_success_url(self) -> str:
        return reverse("question_create")

    def get(self, request, *args: str, **kwargs):
        self.pk = kwargs['pk']
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['test'] = Test.objects.get(pk=self.pk)
        m2m = TestQuestions_m2m.objects.filter(test_id=self.pk).values_list('question_id')
        data['questions'] = []

        for el in m2m:
            data['questions'].append(Question.objects.get(pk=el[0]))
        return data


class TestCreateView(CreateView):
    model = Test
    template_name = 'test/test_form.html'
    form_class = TestForm
    
    def get_success_url(self, pk) -> str:
        return reverse("question_create", args=[pk])

    def form_valid(self, form):
        test = Test.objects.create(**form.cleaned_data)
        return redirect(self.get_success_url(test.pk))


        