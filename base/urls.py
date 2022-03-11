from unicodedata import name
from django.urls import path
from .views import TaskEdit, Tasks, TaskDetail, TodoLogin
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', TodoLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', Tasks.as_view(), name='task' ),
    path('task/<int:pk>/',TaskDetail.as_view(), name='taskDetail' ),
    path('task-edit/<int:pk>', TaskEdit.as_view(), name='task-edit')
]