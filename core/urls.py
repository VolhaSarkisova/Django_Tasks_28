from django.contrib import admin
from django.urls import path

from core.views import index, tasks


app_name = 'core'

urlpatterns = [
    path('', index, name="index"),
    path('tasks/', tasks, name="tasks"),
]