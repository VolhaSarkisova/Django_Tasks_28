from django import forms
from users.models import Users

INPUT_CLASSES = "w-full py-4 px-6 rounded-xl border"

class SignIn(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('login', 'password', )

        widgets = {
            "login": forms.TextInput(attrs={
                "class": INPUT_CLASSES,
            }),
            "password": forms.PasswordInput(attrs={
                "class": INPUT_CLASSES,
            }),
        }

class SignUp(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('login', 'mail', 'password',)

        widgets = {
            "login": forms.TextInput(attrs={
                "class": INPUT_CLASSES,
            }),
            "mail": forms.EmailInput(attrs={
                "class": INPUT_CLASSES,
            }),
            "password": forms.PasswordInput(attrs={
                "class": INPUT_CLASSES,
            }),
        }
