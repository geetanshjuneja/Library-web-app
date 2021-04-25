from django.db import models
from .forms import RegisterForm
from django import forms


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    summary = models.CharField(max_length=500)
    isbn = models.IntegerField()

    def __str__(self):
        return self.title +'-'+ self.publisher

#class UserType(models.Model):
   # book = forms.ForeignKey(RegisterForm,on_delete=models.CASCADE)     