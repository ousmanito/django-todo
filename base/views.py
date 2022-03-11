from dataclasses import field
from multiprocessing import context
from pyexpat import model
from re import template
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task

class Tasks(LoginRequiredMixin,
generic.ListView):
    model = Task
    template_name = 'base/tasks.html'
    context_object_name = 'tasks'

class TaskDetail(LoginRequiredMixin,
generic.DetailView):
    model = Task
    template_name = 'base/task.html'
    context_object_name = 'task'
    field = '__all__'

class TodoLogin(views.LoginView):
    template_name = 'base/login.html'
    field = '__all__'
    redirect_authenticated_user = True


    def get_success_url(self):
        return reverse_lazy('task')

class TaskEdit(LoginRequiredMixin, generic.edit.UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'base/task-edit.html'
    context__object_name = 'task-edit'
    success_url = reverse_lazy('task')