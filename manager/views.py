from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import generic

from manager.forms import TaskSearchForm, TaskUpdateForm, TaskFormCreate, WorkerSearchForm, WorkerCreateForm, \
    WorkerUpdateForm, TaskTypesSearchForm
from manager.models import Task, Worker, TaskType


# Create your views here.

def index(request):
    return render(request, 'pages/index.html')


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "pages/task_list.html"
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = TaskSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Task.objects.all()
        form = TaskSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = "pages/task_detail.html"


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    template_name = "pages/task_form.html"
    form_class = TaskUpdateForm
    success_url = reverse_lazy("manager:tasks-list")



class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    template_name = "pages/task_form.html"
    form_class = TaskFormCreate
    success_url = reverse_lazy("manager:tasks-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("manager:tasks-list")
    template_name = "pages/task_confirm_delete.html"


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    template_name = "pages/worker_list.html"
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = WorkerSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        queryset = get_user_model().objects.all()
        form = WorkerSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(username__icontains=form.cleaned_data["username"])
        return queryset


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    template_name = "pages/worker_detail.html"


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    success_url = reverse_lazy("manager:worker-list")
    template_name = "pages/worker_form.html"
    form_class = WorkerCreateForm


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    success_url = reverse_lazy("manager:worker-list")
    template_name = "pages/worker_form.html"
    form_class = WorkerUpdateForm

class TaskTypesListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    template_name = "pages/task_types_list.html"
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskTypesListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = TaskTypesSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = TaskType.objects.all()
        form = TaskTypesSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class TaskTypesDetailView(LoginRequiredMixin, generic.DetailView):
    model = TaskType
    template_name = "pages/task_types_detail.html"


class TaskTypesCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    template_name = "pages/task_types_form.html"
    fields = "__all__"
    success_url = reverse_lazy("manager:task-types-list")


class TaskTypesUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("manager:task-types-list")
    template_name = "pages/task_types_form.html"


class TaskTypesDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("manager:task-types-list")
    template_name = "pages/task_types_confirm_delete.html"