from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Task

class TaskViewSetTest(APITestCase):
    def setUp(self):
        Task.objects.create(title='Tarea 1', description='Descripción 1', email='email1@example.com')
        Task.objects.create(title='Tarea 2', description='Descripción 2', email='email2@example.com')

    def test_list_tasks(self):
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_task(self):
        url = reverse('task-list')
        data = {'title': 'Nueva Tarea', 'description': 'Descripción Nueva', 'email': 'emailnuevo@example.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 3)
        self.assertEqual(Task.objects.get(id=3).title, 'Nueva Tarea')

    # Añadir más tests para 'retrieve', 'update', 'partial_update', 'delete'

    def test_retrieve_task(self):
        url = reverse('task-detail', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Tarea 1')
        
    def test_update_task(self):
        url = reverse('task-detail', args=[1])
        data = {'title': 'Tarea 1 Modificada', 
                'description': 'Descripción 1 Modificada', 
                'email': 'mail@actiualizado.com'}
        
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get(id=1).title, 'Tarea 1 Modificada')
        
        
