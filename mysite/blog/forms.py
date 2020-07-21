from .models import Comment, Post
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


class PostForm(Form):
    title = CharField(max_length=25,
                     widget=TextInput(attrs={
                         'class': 'form-control',
                         'placeholder': 'Enter a title of article',
                     }))
    author = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your name',
    }))
    email = EmailField(widget=EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your email',
    }))
    content = CharField(required=False, widget=Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Enter content of the article',
    }))


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
