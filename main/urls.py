from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate

urlpatterns = [
    path('', TaskList.as_view(), name="task-list"), # ---> url for displaying task list page.
    path('task/<int:pk>', TaskDetail.as_view(), name='task'), # ---> url for displaying detail of task.
    path('task-create', TaskCreate.as_view(), name='task-create'), # ---> url for form of creating task.

]
