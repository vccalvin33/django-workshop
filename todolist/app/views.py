from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import TaskForm
from .models import Task

# Create your views here.
def home(request):

    tasks = Task.objects.filter(task_owner = request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(False)
            new_task.task_owner = request.user
            new_task.save()
            messages.success(request, "New Task Added!")
            return redirect('/')
    else:
        form = TaskForm()

    context = {
        'tasks': tasks,
        'form': form
    }

    return render(request, 'app/home.html', context)


