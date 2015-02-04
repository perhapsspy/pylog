# -*- coding: utf-8 -*-
from django.shortcuts import render
from blog.models import Post


def home(request):
    template_name = 'home.html'
    posts = Post.objects.all()
    context_data = {'object_list': posts}
    return render(request, template_name, context_data)
