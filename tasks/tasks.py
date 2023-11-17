from celery import shared_task
from django.core.mail import send_mail
<<<<<<< HEAD:task/tasks.py

@shared_task
def notify_email(email, message):
    send_mail(
        'Notificación de tarea',
        message,
        'from@example.com',
        [email],
        fail_silently=False
    )
=======
from django.conf import settings

@shared_task
def send_email_task(subject, message, to_email):
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [to_email],
        fail_silently=False,
    )
>>>>>>> edit_branch:tasks/tasks.py
