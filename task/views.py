from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Task
from .tasks import notify_email

def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/list.html', {'tasks': tasks})


def create_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        task = Task(title=title, description=description)
        task.save()
        
        # Enviar notificación 
        notify_email.delay(task.email, 'Nueva tarea creada')
        
        return HttpResponseRedirect('/tasks')
    
    return render(request, 'tasks/create.html')


def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.save()

        # Enviar notificación
        notify_email.delay(task.email, 'Tarea actualizada')
        
        return HttpResponseRedirect('/tasks')

    return render(request, 'tasks/update.html', {'task': task})


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return HttpResponseRedirect('/tasks')