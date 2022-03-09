from unicodedata import name
from django.urls import path
from .views import Tasks, TaskDetail

urlpatterns = [
    path('', Tasks.as_view(), name='task' ),
    path('task/<int:pk>/',TaskDetail.as_view(), name='taskDetail' )
]