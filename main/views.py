from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Task

# Create your views here.

class TaskList(ListView):
    """
    This class is used for displaying list of Task using ListView.
    """
    model = Task 
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    """
    This class is used for displaying details of particular task using DetailView.
    """
    model = Task
    context_object_name = 'task'
    template_name = 'main/task.html'

class TaskCreate(CreateView):
    """
    This class is used for creating a new task.
    """
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task-list')
