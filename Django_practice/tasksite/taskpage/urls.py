from django.urls import path
from . import views

# app_name = "taskpage"
urlpatterns = [
    path("", views.index, name="index"),
    path('saveuser/', views.saveUser, name="saveuser"),
    path('users-listing/', views.users, name='users-listing'),
    path('<int:x>/task-listing/', views.tasks, name='task-listing'),
    path('<int:user_id>/saveTask/', views.saveTask, name='saveTask'),
    path('<int:task_id>/deleteTask/', views.deleteTask, name='deleteTask'),
    path('<int:task_id>/updateTask/', views.updateTask, name='updateTask'),

]