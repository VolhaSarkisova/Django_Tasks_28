from django.shortcuts import render

from tasks.models import Tasks
from users.models import Users


# Create your views here.
def index(requests):

    return render(requests, 'core/index.html')

def tasks(requests):
    tasks_all = Tasks.objects.all()
    users_all = Users.objects.all()
    context = {
        "tasks": tasks_all,
        "users": users_all
    }
    return render(requests, 'core/tasks.html', context)
