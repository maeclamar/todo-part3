from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, render, redirect
from .models import Blog, Comment, Reply
from . import forms

# Create your views here.

def index(request):
    blogs = Blog.objects.order_by('-created_date')
    return render(request, 'blogs/index.html',{'blogs':blogs})


def detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    comments = Comment.objects.filter(post=blog)
    replies = []
    for comment in comments:
        reply = Reply.objects.filter(comment=comment)
        replies.extend(reply)

    if request.method == "POST": #
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = blog
            comment.author = request.user
            comment.save()
            form = forms.CommentForm()
    else:
        form = forms.CommentForm()

    
    return render(request, 'blogs/detail.html', {'blog': blog, 'form':form, 'comments':comments, 'replies':replies})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            input_username = form.cleaned_data['username']
            input_password = form.cleaned_data['password1']

            new_user = authenticate(username=input_username, password=input_password)

            if new_user is not None:
                login(request, new_user)
                return redirect('blogs:index')
    else:
        form = UserCreationForm()
    return render(request,'blogs/signup.html', {'form': form})
