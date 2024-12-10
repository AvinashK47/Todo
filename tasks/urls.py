from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskList, name='taskList'),
    path('add/', views.AddTask, name='addTask'),
]
