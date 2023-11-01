from django.contrib import admin
from django.urls import path

from manager.views import (
    index,
    tasks_list,
    TaskListView,
)

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="tasks-list"),
]

app_name = "manager"

