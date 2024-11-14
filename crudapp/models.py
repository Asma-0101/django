from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class Journal(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    day_type = models.CharField(max_length=10)
    day_date = models.DateField()
    description = models.TextField(max_length=500)
    day_rate = models.IntegerField()
    privacy_check = models.BooleanField(default=False)
    username = models.ForeignKey(User, default=None, on_delete=models.CASCADE)