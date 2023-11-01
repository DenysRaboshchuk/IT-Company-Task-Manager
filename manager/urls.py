from django.contrib import admin
from django.urls import path

from manager.views import (
    index,
    TaskListView,
    TaskDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="tasks-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="tasks-detail"),
]

app_name = "manager"

