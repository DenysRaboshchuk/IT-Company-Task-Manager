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
    TaskTypesListView,
    TaskTypesDetailView,
    TaskTypesCreateView,
    TaskTypesUpdateView,
    TaskTypesDeleteView,
    PositionListView,
    PositionCreateView,
    PositionDetailView,
    PositionUpdateView,
    PositionDeleteView,
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
    path("task-types/", TaskTypesListView.as_view(), name="task-types-list"),
    path("task-types/<int:pk>/", TaskTypesDetailView.as_view(), name="task-types-detail"),
    path("task-types/create/", TaskTypesCreateView.as_view(), name="task-types-create"),
    path("task-types/<int:pk>/update/", TaskTypesUpdateView.as_view(), name="task-types-update"),
    path("task-types/<int:pk>/delete/", TaskTypesDeleteView.as_view(), name="task-types-delete"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("positions/create/", PositionCreateView.as_view(), name="position-create"),
    path("positions/<int:pk>/", PositionDetailView.as_view(), name="position-detail"),
    path("positions/<int:pk>/update/", PositionUpdateView.as_view(), name="position-update"),
    path("positions/<int:pk>/delete/", PositionDeleteView.as_view(), name="position-delete"),
]

app_name = "manager"

