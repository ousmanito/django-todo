from dataclasses import field
from pyexpat import model
from re import template
from unicodedata import name
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

from .models import Task

class Tasks(generic.ListView):
    model = Task
    template_name = 'base/tasks.html'
    context_object_name = 'tasks'

class TaskDetail(generic.DetailView):
    model = Task
    template_name = 'base/task.html'
    context_object_name = 'task'
    field = '__all__'
