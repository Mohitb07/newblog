from django.db import models
from django.forms.widgets import Widget
from django.core.exceptions import ValidationError

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=40)
    
    def  __str__(self):
        return self.name

class Article(models.Model):
    title=models.CharField(max_length=50)
    createdAt=models.DateTimeField(auto_now_add=True)
    content=models.TextField()
    authors=models.ManyToManyField('Author')
    category = models.CharField(max_length=255, default="Gaming")

    def __str__(self):
        return self.title
