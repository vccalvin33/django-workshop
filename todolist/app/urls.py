from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('tasks/<str:task_id>/edit', views.edit, name="edit-task"),
    path('tasks/<str:task_id>/delete', views.delete, name="delete-task"),
    path('tasks/<str:task_id>/complete', views.complete, name="complete-task"),
]
