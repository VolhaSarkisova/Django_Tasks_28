from django.shortcuts import render, redirect
from core.forms import SignUpForm
from tasks.models import Tasks
from django.contrib.auth.models import User


# Create your views here.
def index(requests):
    tasks = Tasks.objects.all()
    users = User.objects.all()

    context = {
        "tasks": tasks,
        "users": users,
    }
    return render(requests, 'tasks/tasks.html', context)

def start(request):
    return render(request, 'core/start.html')

# def sign_up(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.username = request.user
#             form.save()
#
#             return redirect('/tasks/')
#     else:
#         form = SignUpForm()
#
#     context = {
#         "form": form,
#     }
#
#     return render(request, 'core/sign_up.html', context)






