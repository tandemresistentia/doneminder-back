from django.urls import path,include
from .views import TaskList,FinishedTaskList

urlpatterns = [
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/finished', FinishedTaskList.as_view(), name='finished-task-list'),
]