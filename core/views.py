from django.shortcuts import render

from tasks.models import Tasks
from users.models import Users


# Create your views here.
def index(requests):

    return render(requests, 'core/index.html')


