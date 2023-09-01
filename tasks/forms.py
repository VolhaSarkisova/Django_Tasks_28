from django import forms
from .models import Tasks

INPUT_CLASSES = "w-full py-4 px-6 rounded-xl border"


class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('name', 'description', 'users', 'date_completion', )

        widgets = {
            "name": forms.TextInput(attrs={
                "class": INPUT_CLASSES,
            }),
            "description": forms.TextInput(attrs={
                "class": INPUT_CLASSES,
            }),
            "users": forms.Select(attrs={
                "class": INPUT_CLASSES,
            }),
            "date_completion": forms.DateTimeInput(attrs={
                "class": INPUT_CLASSES,
            }),
        }
class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('name', 'description', 'users', 'status', 'date_completion', )

        widgets = {
            "name": forms.TextInput(attrs={
                "class": INPUT_CLASSES,
            }),
            "description": forms.TextInput(attrs={
                "class": INPUT_CLASSES,
            }),
            "users": forms.Select(attrs={
                "class": INPUT_CLASSES,
            }),
            "status": forms.Select(attrs={
                "class": INPUT_CLASSES,
            }),
            "date_completion": forms.DateTimeInput(attrs={
                "class": INPUT_CLASSES,
            }),
        }


