# from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Post


class PostList(ListView):
    model = Post
    ordering = '-pk'
    template_name = 'blog/post_list.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
