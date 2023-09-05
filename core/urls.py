# from django.contrib.auth import views as auth_views
from django.urls import path, include
from core.views import index,  start
# from .forms import SignInForm


app_name = 'core'

urlpatterns = [
    path('', start, name="index"),
    # path('signup/', sign_up, name="signup"),
    # path(
    #     "signin/",
    #     auth_views.LoginView.as_view(
    #         template_name='core/sign_in.html',
    #         authentication_form=SignInForm
    #     ),
    #     name="login"
    # ),
    path('tasks/', include('tasks.urls')),
]

