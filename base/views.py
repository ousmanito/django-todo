from dataclasses import field, fields
from multiprocessing import context
from pyexpat import model
from re import template
from urllib import request
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth import views, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

from .models import Task

class Tasks(LoginRequiredMixin,
generic.ListView):
    model = Task
    template_name = 'base/tasks.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        return context

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
    fields = ['title', 'details', 'completed']
    template_name = 'base/task-edit.html'
    context__object_name = 'task-edit'
    success_url = reverse_lazy('task')


class NewTask(LoginRequiredMixin, generic.edit.CreateView):
    model = Task
    fields = ['title', 'details', 'completed']
    context_object_name = 'new-task'
    template_name = 'base/new-task.html'
    success_url = reverse_lazy('task')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class TaskDelete(LoginRequiredMixin, generic.edit.DeleteView):
    model = Task
    template_name = 'base/task-delete.html'
    success_url = reverse_lazy('task')


class TodoRegister(generic.edit.FormView):
    form_class = UserCreationForm
    fields = '__all__'
    template_name = 'base/register.html'
    success_url = reverse_lazy('task')


    def form_valid(self, form):   
            user = form.save()
            if user is not None:
                login(self.request, user)
                return super().form_valid(form)
