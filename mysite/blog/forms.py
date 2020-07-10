from .models import Comment
from django.forms import ModelForm, TextInput, Textarea, EmailInput


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'email', 'body')
        widgets = {
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter name',
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
            }),
            'body': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter comment',
            }),
        }
