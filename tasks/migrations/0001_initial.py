<<<<<<< HEAD:task/migrations/0001_initial.py
# Generated by Django 4.2.7 on 2023-11-16 21:54
=======
# Generated by Django 4.2.7 on 2023-11-16 23:51
>>>>>>> edit_branch:tasks/migrations/0001_initial.py

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD:task/migrations/0001_initial.py
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
=======
                ('title', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
>>>>>>> edit_branch:tasks/migrations/0001_initial.py
            ],
        ),
    ]