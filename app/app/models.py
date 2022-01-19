from django.db import models


class Application(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Command(models.Model):
    command = models.CharField(max_length=255, unique=True, db_index=True, null=False)

    def __str__(self):
        return self.command


class TaskApplication(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='task_application_set')
    command = models.ForeignKey(Command, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    task_application = models.ForeignKey(TaskApplication, on_delete=models.CASCADE)
    status_choices = (
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('failed', 'Failed'),
    )
    status = models.CharField(max_length=200, choices=status_choices, default='new', db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status

