from django.urls import path

from tasks.views import task_detail

app_name = 'task'

urlpatterns = [
    path("<int:pk>/", task_detail, name="detail"),
]