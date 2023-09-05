from django.urls import path

from users.views import sign_in

app_name = 'users'

urlpatterns = [
    path('', sign_in, name='sign_in'),
    ]