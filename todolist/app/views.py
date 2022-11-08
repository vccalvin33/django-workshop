from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from .forms import TaskForm
from .models import Task

# Create your views here.
def signup_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username Taken!")
                return redirect('signup')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email Taken!")
                    return redirect('signup')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    messages.success(request, "Registered!")
                    return redirect('login')
        else:
            messages.error(request, "Passwords Don't Match!")
            return redirect('signup')
    else:
        return render(request, 'app/signup.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def delete(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        task.delete()
        messages.success(request, "Task Deleted!")
        return redirect('/')

    return render(request, 'app/delete.html')

@login_required(login_url='login')
def complete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_completed = not task.is_completed
    task.save()
    messages.success(request, "Task Completed!")
    return redirect('/')