from django.contrib.auth.models import AbstractUser
from django.db import models

from IT_Company_Task_Manager import settings


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return self.name


class Task(models.Model):
    priority_chooses = [
        ("ASAP", "ASAP"),
        ("HP", "High Priority"),
        ("LP", "Low Priority"),
    ]
    name = models.CharField(max_length=255)
    deadline = models.DateField()
    is_complited = models.BooleanField(
        blank=True,
        default=False,
    )
    description = models.TextField()
    priority = models.CharField(max_length=255, choices=priority_chooses) #
    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.CASCADE,
        related_name="tasks"
    )
    assignees = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="tasks",
    )

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name="workers",
    )

    def __str__(self):
        return f"{self.position}: {self.username} ({self.first_name} {self.last_name})"


