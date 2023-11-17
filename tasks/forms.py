from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'email', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Título'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Correo electrónico'}),
            'description': forms.Textarea(attrs={'placeholder': 'Descripción'}),
        }