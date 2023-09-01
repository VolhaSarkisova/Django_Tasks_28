from django.urls import path

from tasks.views import task_detail, tasks, new_task, edit_task, delete_task

app_name = 'task'

urlpatterns = [
    path('', tasks, name='tasks'),
    path("new/", new_task, name="new_item"),
    path("<int:pk>/", task_detail, name="detail"),
    path("<int:pk>/edit/", edit_task, name="edit"),
    path("<int:pk>/delete/", delete_task, name="delete"),
]