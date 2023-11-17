from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_tasks, name='list_tasks'),
    path('new/', views.create_task, name='create_task'),
    path('<int:pk>/edit/', views.update_task, name='update_task'),
    path('<int:pk>/delete/', views.delete_task, name='delete_task'),
]