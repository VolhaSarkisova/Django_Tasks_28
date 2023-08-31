from django.shortcuts import render, get_object_or_404

from tasks.models import Tasks


def task_detail(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    context = {
        "task": task,
    }
    return render(request, 'tasks/detail.html')



