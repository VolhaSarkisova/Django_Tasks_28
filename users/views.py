from django.shortcuts import render, redirect, get_object_or_404
from users.forms import SignIn, SignUp
from users.models import Users


# Create your views here.
def sign_in(request):
    users = Users.objects.all()
    form = SignIn(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            for user in users:
                if form.cleaned_data['login'] == user.login \
                    and form.cleaned_data['password'] == user.password:
                    return redirect('/tasks/')

    context = {
        "form": form
    }
    return render(request, 'users/signin.html', context)

def sign_up(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.username = request.user
            form.save()

            return redirect('users:sign_in')
    else:
        form = SignUp()

    context = {
        "form": form,
    }

    return render(request, 'users/signup.html', context)

