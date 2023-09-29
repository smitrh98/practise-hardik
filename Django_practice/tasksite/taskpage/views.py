from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from taskpage.models import User, Task
from django.utils import timezone
from django.views import View
from django.views.generic import ListView


class Index(View):

    def get(self, request):
        context = {'name': "Hardik"}
        return render(request, "taskpage/index.html",context)


class SaveUser(View):

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        message = request.POST.get('message')
        User.objects.create(user_name = name,email = email, phone_number=phone, country=country, message=message, date= timezone.now())
        return redirect('users-listing')


class Users(View):

    def get(self, request):
        users = User.objects.all()
        context = {'users' : users}
        return render(request, "taskpage/users.html", context)

    
class TasksDetail(ListView):
    model = Task
    queryset = Task.objects.all()
    template_name = "taskpage/task.html"
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        obj = super().get_context_data(**kwargs)
        obj['id'] = self.kwargs.get('pk')
        obj['users'] = User.objects.all()
        return obj
    
    def get_queryset(self) -> QuerySet[Any]:
        qry= super().get_queryset()
        queryset= qry.filter(user_id=self.kwargs.get('pk')).order_by('-date')
        return queryset


class SaveTask(View):   
    
    def post(self, request,**kwargs):
        user_id = kwargs.get('user_id')
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        asign = request.POST.getlist('asign')
        users = User.objects.filter(id__in=asign)
        instance=Task.objects.create(user_id = user_id, title = title, description = description, status = status, date = timezone.now())
        instance.asign.set(users)
        return redirect('task-listing', pk=user_id)


class DeleteTask(View):

    def get(self, request, **kwargs):
        task_id = kwargs.get('task_id')
        deltask = Task.objects.get(id=task_id)
        deltask.delete()
        return redirect('task-listing', pk=deltask.user_id)


class UpadateTask(View):

    def post(self, request, **kwargs):
        task_id = kwargs.get('task_id')
        status = request.POST.get('status')
        uTask = Task.objects.get(id=task_id)
        uTask.status = status
        uTask.save()
        return redirect('task-listing', pk=uTask.user_id)
    
