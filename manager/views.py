from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from manager.models import Task


# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

@login_required
def tasks_list(request):
    tasks_list = Task.objects.all()
    context = {
        "tasks_list": tasks_list
    }
    return render(request, 'pages/tasks_list.html', context=context)


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "pages/tasks_list.html"
    paginate_by = 10

