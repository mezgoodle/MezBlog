from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create()
        Post.objects.create(
            title='first post',
            slug='first-post',
            author=user,
            content='body of the first post',
        )

    def test_title_content(self):
        todo = Post.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEquals(expected_object_name, 'first post')

    def test_body_content(self):
        todo = Post.objects.get(id=1)
        expected_object_name = f'{todo.content}'
        self.assertEquals(expected_object_name, 'body of the first post')

    def test_slug_content(self):
        todo = Post.objects.get(id=1)
        expected_object_name = f'{todo.slug}'
        self.assertEquals(expected_object_name, 'first-post')
