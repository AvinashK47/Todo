from django.shortcuts import render ,redirect

# Create your views here.

from .models import Task
from .forms import TasksForm

def TaskList(request):
    tasks = Task.objects.all()
    return render(request,'tasks/taskList.html',{'tasks':tasks})

def AddTask(request):
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = TasksForm()
    return render(request,'tasks/addTask.html',{'form':form})