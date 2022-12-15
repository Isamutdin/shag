from django.db import models
from tests.models import Question

# Create your models here.
class InputAnswer(models.Model):#one string
    right_answer = models.CharField(max_length=100)
    input_answer = models.CharField(max_length=100, blank=True)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)


class ChoiceAnswer(models.Model):#radio/check answer
    is_right = models.BooleanField(default=False)
    label = models.CharField(max_length=30)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)


class FileAnswer(models.Model):
    is_right = models.BooleanField(default=False)
    file = models.FileField()
    question = models.ForeignKey(Question, on_delete=models.PROTECT)


class TextAnswer(models.Model):
    is_right = models.BooleanField(default=False)
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.PROTECT)

