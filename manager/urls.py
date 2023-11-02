from django.contrib import admin
from django.urls import path

from manager.views import (
    index,
    TaskListView,
    TaskDetailView,
    TaskUpdateView,
    TaskCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="tasks-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="tasks-detail"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="tasks-update"),
    path("tasks/create/", TaskCreateView.as_view(), name="tasks-create"),
]

app_name = "manager"

