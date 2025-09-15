from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', { 'form':form })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('alltask')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', { 'form':form })

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def all_task(request):
    tasks = Todo.objects.filter(user=request.user)
    return render(request, "curd/tasks.html", {"tasks": tasks})

def create_task(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('alltask')
    else:
        form = TodoForm()
    return render(request, 'curd/create.html', {'form':form})

def update_task(request, pk):
    task = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('alltask')
    else:
        form = TodoForm(instance=task)        
    return render(request, 'curd/update.html', { 'task':task, 'form':form })

def delete_task(request, pk):
    task = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('alltask')
    return render(request, 'curd/delete.html', { 'task':task })

def detail_task(request, pk):
    task = get_object_or_404(Todo, pk=pk)
    return render(request, 'curd/detail.html', { 'task':task })

def search_task(request):
    query = request.GET.get('q','')
    if query:
        tasks = Todo.objects.filter( Q(title__icontains=query) | Q(status__icontains=query))
    else:
        tasks = Todo.objects.all()
    return render(request, 'curd/tasks.html', { 'tasks':tasks,'query':query })
