from django.urls import path
from . import views

# app_name = "taskpage"
urlpatterns = [
    path("user", views.Index.as_view(), name="index"),
    path('saveusercl/', views.SaveUser.as_view(), name="saveuser"),
    path('users-listingcl/', views.Users.as_view() , name='users-listing'),
    path('<int:pk>/task-listingcl/', views.TasksDetail.as_view(), name='task-listing'),
    path('<int:user_id>/saveTaskcl/', views.SaveTask.as_view(), name='saveTask'),
    path('<int:task_id>/deleteTaskcl/', views.DeleteTask.as_view(), name='deleteTask'),
    path('<int:task_id>/updateTaskcl/', views.UpadateTask.as_view(), name='updateTask'),

]