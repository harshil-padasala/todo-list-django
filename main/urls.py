from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(next_page='login'), name="logout"),
    path('', TaskList.as_view(), name="task-list"), # ---> url for displaying task list page.
    path('task/<int:pk>', TaskDetail.as_view(), name='task'), # ---> url for displaying detail of task.
    path('task-create', TaskCreate.as_view(), name='task-create'), # ---> url for form of creating task.
    path('task-update/<int:pk>', TaskUpdate.as_view(), name='task-update'), # ---> url for updating a task
    path('task-delete/<int:pk>', TaskDelete.as_view(), name='task-delete'),
]
