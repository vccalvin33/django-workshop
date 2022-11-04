from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


from .forms import TaskForm
from .models import Task

# Create your views here.
@login_required(login_url='login')
def home(request):

    tasks = Task.objects.filter(task_owner = request.user).order_by('deadline')

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

def edit(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task Updated!")
            return redirect('/')
    else:
        form = TaskForm(instance=task)

    context = {
        'form': form
    }

    return render(request, 'app/edit.html', context)

def delete(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        task.delete()
        messages.success(request, "Task Deleted!")
        return redirect('/')

    return render(request, 'app/delete.html')

def complete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_completed = not task.is_completed
    task.save()
    messages.success(request, "Task Completed!")
    return redirect('/')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged In!")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials!")
            print("user not found")
            return redirect('login')
    return render(request, 'app/login.html')

def logout_user(request):
    print('function is called')
    logout(request)
    messages.success(request, "Logged Out!")
    return redirect('login')