from django.urls import path
from .feeds import LatestPostsFeed, AtomSiteNewsFeed
from . import views

urlpatterns = [
    path('', views.PostList, name='home'),
    path('<slug:slug>/', views.PostDetail, name='post_detail'),
    path('feed/rss', LatestPostsFeed(), name='post_feed'),
    path('feed/atom', AtomSiteNewsFeed()),
]
