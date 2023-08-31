from django.shortcuts import render, get_object_or_404

from tasks.models import Tasks
from users.models import Users


def task_detail(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    context = {
        "task": task,
    }
    return render(request, 'tasks/detail.html')



def tasks(requests):
    tasks_all = Tasks.objects.all()
    users_all = Users.objects.all()
    context = {
        "tasks": tasks_all,
        "users": users_all
    }
    return render(requests, 'core/tasks.html', context)