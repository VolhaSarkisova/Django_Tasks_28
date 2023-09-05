from django.urls import path

from users.views import sign_in, sign_up

app_name = 'users'

urlpatterns = [
    path('', sign_in, name='sign_in'),
    path('signup/', sign_up, name="sign_up"),
    ]