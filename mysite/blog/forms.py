from .models import Comment
from django.forms import ModelForm, TextInput, Textarea, EmailInput, Form, CharField, EmailField


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


class EmailPostForm(Form):
    name = CharField(max_length=25,
                     widget=TextInput(attrs={
                         'class': 'form-control',
                         'placeholder': 'Enter name',
                     }))
    email = EmailField(widget=EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your email',
    }))
    to = EmailField(widget=EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter email',
    }))
    comments = CharField(required=False, widget=Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Your comments',
    }))
