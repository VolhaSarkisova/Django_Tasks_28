from urllib.request import Request

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from comments.forms import CommentForm
from comments.models import Comments
from tasks.models import Tasks


@login_required()
def task_comments(request: Request, pk, parent):
    task = get_object_or_404(Tasks, pk=pk)
    comments = Comments.objects.filter(task=task)
    if parent!= 0:
        parent_comment = f"Reply to comment: {get_object_or_404(Comments, id=parent)}"
    else:
        parent_comment = f"Task commentary: {task.name}"
    print(request.method)
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task_id = pk
            # comment.user = request.user

            # if parent != 0:
            #     comment.parent = parent
            try:
            # id integer e.g. 15
                parent_id = int(parent)
            except:
                parent_id = None
            # if parent_id has been submitted get parent_obj id
            if parent_id:
                parent_obj = Comments.objects.get(id=parent_id)
                # if parent object exist
                if parent_obj:
                    # create replay comment object
                    replay_comment = form.save(commit=False)
                    # assign parent_obj to replay comment
                    replay_comment.parent = parent_obj
            comment.save()
        return redirect("comments:comments", pk=pk, parent=parent)
    else:
        form = CommentForm()
    context = {
        "form": form,
        "comments": comments,
        "task": task,
        "parent_comment": parent_comment
    }
    return render(request, "comments/detail.html", context)
