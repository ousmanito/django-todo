from audioop import add
from email.policy import default
from typing import Text
from urllib import request
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.forms import BooleanField, CharField, DateTimeField

class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name="Titre")
    details = models.TextField(blank=True, verbose_name="Détails")
    date = models.DateTimeField(auto_now_add=False, verbose_name="Date d'échéance")
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.title


