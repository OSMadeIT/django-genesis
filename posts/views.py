# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Posts
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    posts = Posts.objects.all()[:10]
    context = {
        'title': 'Latest Posts',
        'posts': posts
    }
    return render(request, 'posts/index.html', context)


def details(request,id):
    post = Posts.objects.get(id=id)

    context = {
        'post': post
    }
    return render(request, 'posts/details.html', context)

@login_required(login_url='/accounts/login')
def create_post(request):
    return render(request, 'posts/create_post.html')
