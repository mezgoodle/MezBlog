from django.test import TestCase
from .models import Post, Comment
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


class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create()
        Post.objects.create(
            title='first post',
            slug='first-post',
            author=user,
            content='body of the first post',
        )
        post = Post.objects.get(id=1)
        Comment.objects.create(
            post=post,
            author='mezgoodle',
            email='mezgoodle@gmail.com',
            body='test comment',
        )

    def test_author_content(self):
        todo = Comment.objects.get(id=1)
        expected_object_name = f'{todo.author}'
        self.assertEquals(expected_object_name, 'mezgoodle')

    def test_body_content(self):
        todo = Comment.objects.get(id=1)
        expected_object_name = f'{todo.body}'
        self.assertEquals(expected_object_name, 'test comment')

    def test_active_content(self):
        todo = Comment.objects.get(id=1)
        expected_object_name = f'{todo.active}'
        self.assertEquals(expected_object_name, 'False')
