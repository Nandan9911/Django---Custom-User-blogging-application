from django.urls import path
from .views import (
    PostListView,
    PostCreateView,
    )
from . import views




urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about')
]