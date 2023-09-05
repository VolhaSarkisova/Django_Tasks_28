from django.shortcuts import render, redirect
from users.forms import SignIn
from users.models import Users


# Create your views here.
def sign_in(request):
    users = Users.objects.all()
    if request.method == 'POST':
        form = SignIn(request.POST)
        if form.is_valid():
            return redirect('/tasks/')

    else:
        form = SignIn()

    context = {
        "form": form,
        "users": users
    }

    return render(request, 'users/signin.html', context)

