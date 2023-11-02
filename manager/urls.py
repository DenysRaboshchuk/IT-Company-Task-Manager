from django.contrib import admin
from django.urls import path

from manager.views import (
    index,
    TaskListView,
    TaskDetailView,
    TaskUpdateView,
    TaskCreateView,
    TaskDeleteView,
    WorkerListView,
    WorkerDetailView,
    WorkerCreateView,
    WorkerUpdateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="tasks-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="tasks-detail"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="tasks-update"),
    path("tasks/create/", TaskCreateView.as_view(), name="tasks-create"),
    path("tasks/<int:pk>/confirmation-delete-task/", TaskDeleteView.as_view(), name="tasks-delete"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("workers/<int:pk>/update/", WorkerUpdateView.as_view(), name="worker-update"),
]

app_name = "manager"

