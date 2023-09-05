from django import forms
from comments.models import Comments

INPUT_CLASSES = "w-full py-4 px-6 rounded-xl border"
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)

        widgets = {
            # 'parent': forms.Select(attrs={
            #     "class": INPUT_CLASSES,
            # }),
            'text': forms.TextInput(attrs={
                "class": INPUT_CLASSES,
            })
        }

