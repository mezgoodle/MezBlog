from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList, name='home'),
    path('<slug:slug>/', views.PostDetail, name='post_detail')
]
