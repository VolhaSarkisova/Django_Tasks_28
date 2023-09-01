from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from tasks.models import Tasks
from users.models import Users
from tasks.forms import NewTaskForm, EditTaskForm

def task_detail(request, pk):
    task = get_object_or_404(Tasks, pk=pk)

    context = {
        "task": task,
    }
    return render(request, 'tasks/detail.html', context)

def tasks(request):
    tasks = Tasks.objects.all()
    users = Users.objects.all()
    context = {
        "tasks": tasks,
        "users": users
    }
    return render(request, 'tasks/tasks.html', context)
@login_required()
def new_task(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()

            return redirect("core:task:detail", pk=task.id)
    else:
        form = NewTaskForm()

    context = {
        "form": form,
        "title": "New Item"
    }

    return render(request, "tasks/add.html", context)

@login_required()
def edit_task(request, pk):
    task = get_object_or_404(Tasks, pk=pk)

    if request.method == "POST":
        form = EditTaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()

            return redirect("core:task:detail", pk=task.id)
    else:
        form = EditTaskForm(instance=task)

    context = {
        "form": form,
        "title": "Edit Item"
    }

    return render(request, "tasks/add.html", context)

@login_required()
def delete_task(request, pk):
    task = get_object_or_404(Tasks, pk=pk)

    task.delete()

    return redirect("core:index")

