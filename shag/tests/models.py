from django.db import models

# Create your models here.
class Test(models.Model):
    title = models.CharField(max_length=100)
    
    
    complexity = models.CharField(max_length=10, choices=0)
