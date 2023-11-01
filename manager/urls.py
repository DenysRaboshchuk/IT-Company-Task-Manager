from django.contrib import admin
from django.urls import path

from manager.views import (
    index,
    tasks_list,
)

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", tasks_list, name="tasks-list"),
]

app_name = "manager"

