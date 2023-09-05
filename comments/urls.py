from django.urls import path

from comments.views import task_comments

app_name = 'comments'

urlpatterns = [
    path('<int:pk>/<int:parent>/', task_comments, name='comments'),
]