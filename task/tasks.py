from celery import shared_task
from django.core.mail import send_mail

@shared_task
def notify_email(email, message):
    send_mail(
        'Notificación de tarea',
        message,
        'from@example.com',
        [email],
        fail_silently=False
    )