from django.db import models
from users.models import CustomUser
from ckeditor.fields import RichTextField 

# Create your models here.

class Question(models.Model):
    note = RichTextField()

    score = models.PositiveSmallIntegerField(default=0)

    answer_type = models.ForeignKey('TypeAnswer', on_delete=models.PROTECT)

    def __str__(self) -> str:
        return str(self.note)


class TypeAnswer(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.title


class Test(models.Model):
    COMPLEXITY = (
        ("es", "Easy"),
        ("md", "Medium"),
        ("hr", "Hard")
    )

    title = models.CharField(max_length=30)
    
    note = RichTextField()

    max_score = models.PositiveIntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    complexity = models.CharField(max_length=2, choices=COMPLEXITY)

    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT, blank=True)

    def __str__(self) -> str:
        return self.title


class TestQuestions_m2m(models.Model):
    test = models.ForeignKey("Test", on_delete=models.PROTECT)
    question = models.ForeignKey("Question", on_delete=models.PROTECT)