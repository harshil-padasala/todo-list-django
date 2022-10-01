from django.urls import path
from .views import TaskList, Task

urlpatterns = [
    path('', TaskList.as_view(), name="task list"),
    path('task/<int:pk>', Task.as_view(), name='task')
]
