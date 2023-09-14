from django.shortcuts import render, redirect, get_object_or_404
from taskpage.models import User, Task
from django.utils import timezone


def index(request):
    context = { 'name' : "Hardik"}
    
    return render(request, "taskpage/index.html", context)

def saveUser(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        message = request.POST.get('message')
        en = User(user_name = name,email = email, phone_number=phone, country=country, message=message, date= timezone.now())
        en.save()

    return redirect(users)

def users(request):
    users = User.objects.all()
    context = {'users': users}
    
    return render(request, "taskpage/users.html", context)

def tasks(request,*args,**kwargs):
    id = kwargs.get('x')
    tasks = Task.objects.filter(user_id=id)
    context = {'tasks': tasks , 'id' : id}
    
    return render(request, "taskpage/task.html", context)

def saveTask(request, **kwargs):
    user_id = kwargs.get('user_id')
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        Task.objects.create(user_id = user_id, title = title, description = description, status = status, date = timezone.now())
    
    return redirect(tasks, x=user_id)

def deleteTask(request, **kwargs):
    task_id = kwargs.get('task_id')
    deltask = Task.objects.get(id=task_id)
    deltask.delete()

    return redirect(tasks, x=deltask.user_id)

def updateTask(request, **kwargs):
    task_id = kwargs.get('task_id')
    if request.method == "POST":         
        status = request.POST.get('status')
        uTask = Task.objects.get(id=task_id)
        uTask.status = status
        uTask.save()
        
    return redirect(tasks, x=uTask.user_id)
    
