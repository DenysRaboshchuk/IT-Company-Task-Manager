from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import generic

from manager.forms import TaskSearchForm, TaskForm, TaskFormCreate
from manager.models import Task


# Create your views here.

def index(request):
    return render(request, 'pages/index.html')


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "pages/tasks_list.html"
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
    template_name = "pages/tasks_detail.html"


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    template_name = "pages/task_form.html"
    form_class = TaskForm
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



