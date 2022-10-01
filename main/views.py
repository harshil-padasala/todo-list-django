from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Task

# Create your views here.

class CustomLoginView(LoginView):
    """
    This class is used for login purprse.
    """
    template_name = 'main/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy('task-list')


class RegisterPage(FormView):
    template_name = 'main/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user) 
        return super(RegisterPage, self).form_valid(form)

    # this method is used for block authenticated user to do not register again.
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task-list')
        return super(RegisterPage, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin,ListView):
    """
    This class is used for displaying list of Task using ListView.
    """
    model = Task 
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(is_complete=False).count()

        # to search task in user account
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(task_title__startswith=search_input)

        context['search_input'] = search_input
        return context

class TaskDetail(LoginRequiredMixin,DetailView):
    """
    This class is used for displaying details of particular task using DetailView.
    """
    model = Task
    context_object_name = 'task'
    template_name = 'main/task.html'

class TaskCreate(LoginRequiredMixin,CreateView):
    """
    This class is used for creating a new task.
    """
    model = Task
    fields = ['task_title', 'description', 'is_complete']
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin,UpdateView):
    """
    This class is used for updating a task.
    """
    model = Task
    fields = ['task_title', 'description', 'is_complete']
    success_url = reverse_lazy('task-list')

class TaskDelete(LoginRequiredMixin,DeleteView):
    """
    This class is used for deleting a task.
    """
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task-list')
