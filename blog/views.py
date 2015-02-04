# -*- coding: utf-8 -*-
from django.http.response import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('hi')
