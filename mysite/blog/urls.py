from django.urls import path
from .feeds import LatestPostsFeed, AtomSiteNewsFeed
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostList, name='home'),
    path('<slug:slug>/', views.PostDetail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('feed/rss', LatestPostsFeed(), name='post_feed'),
    path('feed/atom', AtomSiteNewsFeed()),
]
