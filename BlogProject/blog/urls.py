from django.urls import path
from .views import (
    BlogPostListView,
    BlogPostDetailView,
    BlogPostCreateView,
    BlogPostUpdateView,
    BlogPostDeleteView,
)

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blog_list'),
    path('post/<slug:slug>/', BlogPostDetailView.as_view(), name='blog_detail'),
    path('post/new/', BlogPostCreateView.as_view(), name='blog_create'),
    path('post/<slug:slug>/edit/', BlogPostUpdateView.as_view(), name='blog_update'),
    path('post/<slug:slug>/delete/', BlogPostDeleteView.as_view(), name='blog_delete'),
]
