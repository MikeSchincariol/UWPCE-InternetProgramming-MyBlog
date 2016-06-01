from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        # Don't show all fields. Some, like user, we will fill
        # in automagically later.
        fields = ('title',
                  'text')


