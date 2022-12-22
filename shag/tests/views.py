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

    def get_context_data(self, **kwargs):

        data = super().get_context_data(**kwargs)
        data['test'] = Test.objects.get(pk=self.kwargs['pk'])# через урл передается pk теста

        #через таблицу m2m я извлекаю все id вопросов принадлежащие тесту
        data['m2m'] = TestQuestions_m2m.objects.filter(test_id=self.kwargs['pk'])

        return data

    def form_valid(self, form):

        question = Question.objects.create(**form.cleaned_data)#создаю в бд вопрос
        test_question_m2m = TestQuestions_m2m.objects.create(test_id=self.kwargs['pk'], question_id=question.pk)#создаю привязку вопроса к тесту

        question.save()
        test_question_m2m.save()
        return redirect(self.get_success_url())
        

    def get_success_url(self) -> str:
        return reverse("question_create", args=[self.kwargs['pk']]) #передаю пк с тестом на туже стрнаицу


class QuestionUpdateView(UpdateView):
    model = Question
    template_name = "question/question_form.html"
    form_class = QuestionForm

    def get_context_data(self, **kwargs):# тоже самое что и create
        data = super().get_context_data(**kwargs)
        data['test'] = Test.objects.get(pk=self.kwargs['id'])
       
        data['m2m'] = TestQuestions_m2m.objects.filter(test_id=self.kwargs['id'])
        return data

    def get_success_url(self) -> str:#pk вопроса, а id теста
        return reverse("question_create", args=[self.kwargs['id']])


class QuestionDeleteView(DeleteView):
    model = Question
    template_name = "question/question_confirm_delete.html"

    def get_success_url(self) -> str:#id теста
        return reverse("question_create", args=[self.kwargs['id']])


class TestCreateView(CreateView):
    model = Test
    template_name = 'test/test_form.html'
    form_class = TestForm
    
    def get_success_url(self, pk) -> str:
        return reverse("question_create", args=[pk])

    def form_valid(self, form):
        test = Test.objects.create(**form.cleaned_data)
        test.save()
        return redirect(self.get_success_url(test.pk))


class TestUpdateView(UpdateView):
    model = Test
    template_name = 'test/test_form.html'
    form_class = TestForm

    def get_success_url(self) -> str:
        return reverse("question_create", args=[self.kwargs['pk']])


class TestListView(ListView):#list view
    model = Test
    context_object_name = "tests"
    template_name = 'test/lists.html'

