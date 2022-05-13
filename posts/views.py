from django import forms
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm


def index(request):
    form = PostForm(request.POST, request.FILES)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        else:
            return HttpResponseRedirect(form.errors.as_json())

    posts = Post.objects.all().order_by('-created_at')[:20]
    return render(request, 'posts.html', {'posts': posts, 'form': form})


def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')


def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        else:
            return HttpResponseRedirect(form.errors.as_json())
    form = PostForm
    return render(request, 'edit.html', {'post': post, 'form': form})


def likes(request, id):
    liked = Post.objects.get(id=id)
    liked.like_count += 1
    liked.save()
    return HttpResponseRedirect('/')
