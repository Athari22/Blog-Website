# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # URL for the main webpage
    path('users/', views.user_list, name='users'),  # URL for displaying users
    path('blogs/', views.post_list, name='blogs'),  # URL for displaying blog posts
    path('comments/', views.comment_list, name='comments'),  # URL for displaying comments
    path('categories/', views.category_list, name='categories'),  # URL for displaying categories
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),  # URL for a specific blog post
]