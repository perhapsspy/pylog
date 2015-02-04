# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView

from blog.models import Post


class PostList(ListView):
    model = Post
    template_name = 'home.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'detail.html'
