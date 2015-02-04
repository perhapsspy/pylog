# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView, CreateView

from blog.models import Post, Category


class PostList(ListView):
    model = Post
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context

    def get_queryset(self):
        queryset = super(PostList, self).get_queryset()
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category=category_id)
        return queryset


class PostDetail(DetailView):
    model = Post
    template_name = 'detail.html'


class PostCreate(CreateView):
    model = Post
    template_name = 'create.html'
