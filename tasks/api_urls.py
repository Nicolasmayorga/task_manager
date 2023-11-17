# tasks/api_urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

# Asegúrate de que el prefijo para el router sea 'tasks'
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

# Estas son tus rutas de la API
urlpatterns = [
    path('', include(router.urls)),  # La ruta raíz para las URLs incluidas aquí
]
