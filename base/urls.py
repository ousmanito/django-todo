from unicodedata import name
from django.urls import path
from .views import NewTask, TaskDelete, TaskEdit, Tasks, TaskDetail, TodoLogin, TodoRegister, HomeTodo
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', HomeTodo.as_view(), name='home-todo'),
    path('login/', TodoLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home-todo'), name='logout'),
    path('tasks', Tasks.as_view(), name='task' ),
    path('task/<int:pk>/',TaskDetail.as_view(), name='taskDetail' ),
    path('task-edit/<int:pk>', TaskEdit.as_view(), name='task-edit'),
    path('register/', TodoRegister.as_view(), name='register'),
    path('new-task/', NewTask.as_view(), name='new-task'),
    path('task-delete/<int:pk>', TaskDelete.as_view(), name='task-delete'),
]