from django.urls import path

from tasks.views import task_detail, tasks

app_name = 'task'

urlpatterns = [
    path('', tasks, name='tasks'),
    path("<int:pk>/", task_detail, name="detail"),
]