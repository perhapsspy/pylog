# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView, CreateView

from blog.models import Post


class PostList(ListView):
    model = Post
    template_name = 'home.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'detail.html'


class PostCreate(CreateView):
    model = Post
    template_name = 'create.html'
