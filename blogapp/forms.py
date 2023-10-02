from django import forms
from .models import Blog2

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog2
        fields = [
            'image',
            'title',
            'subtitle',
            'text'
        ]

