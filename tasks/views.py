from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import Task
from .forms import TaskForm
from .serializers import TaskSerializer
from .tasks import send_email_task

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Vista para listar tareas
def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/list_tasks.html', {'tasks': tasks})

# Vista para crear una nueva tarea
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            send_email_task.delay(
                'Nueva Tarea Creada',
                f'Tarea "{task.title}" ha sido creada con éxito.',
                task.email
            )
            return redirect('list_tasks')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})

# Vista para actualizar una tarea existente
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            send_email_task.delay(
                'Tarea Actualizada',
                f'Tu tarea "{task.title}" ha sido actualizada.',
                task.email
            )
            return redirect('list_tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/update_task.html', {'form': form})

# Vista para eliminar una tarea existente
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        send_email_task.delay(
            'Tarea Eliminada',
            f'La tarea "{task.title}" ha sido eliminada.',
            task.email
        )
        task.delete()
        return redirect('list_tasks')
    return render(request, 'tasks/delete_task.html', {'task': task})
