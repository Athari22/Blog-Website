# blog/views.py
from django.shortcuts import render
from .models import Post, Comment, Category, User
from . import views

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def user_list(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blogs.html', {'posts': posts})

def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'comments.html', {'comments': comments})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'blogdetails.html', {'post': post})
