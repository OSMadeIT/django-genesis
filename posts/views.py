# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,render
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.


def index(request):
    posts = Post.objects.all()[:10]
    context = {
        'title': 'Latest Posts',
        'posts': posts
    }
    return render(request, 'posts/index.html', context)


def details(request,id):
    post = Post.objects.get(id=id)

    context = {
        'post': post
    }
    return render(request, 'posts/details.html', context)

@login_required(login_url='/accounts/login')
def create_post(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid:
            # save article to db
            return redirect("posts:index")
    else:
        form = forms.CreatePost()
    return render(request, 'posts/create_post.html', {'form': form})
