from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
<<<<<<< HEAD:task/serializers.py
        fields = ('id', 'title', 'description', 'created_at')
=======
        fields = ['id', 'title', 'email', 'description']
>>>>>>> edit_branch:tasks/serializers.py
