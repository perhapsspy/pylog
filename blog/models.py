# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = u'분류'
        ordering = ['name']

    name = models.CharField(verbose_name=u'이름', max_length=50)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    class Meta:
        verbose_name = u'글'
        ordering = ['created']

    category = models.ForeignKey(Category, verbose_name=u'분류', null=True, blank=True)
    title = models.CharField(verbose_name=u'제목', max_length=256)
    content = models.TextField(u'내용', blank=True, default='')
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'생성일')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id})
