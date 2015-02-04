# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\uc774\ub984')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '\ubd84\ub958',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='\uc81c\ubaa9')),
                ('content', models.TextField(default=b'', verbose_name='\ub0b4\uc6a9', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\uc0dd\uc131\uc77c')),
                ('category', models.ForeignKey(verbose_name='\ubd84\ub958', blank=True, to='blog.Category', null=True)),
            ],
            options={
                'ordering': ['created'],
                'verbose_name': '\uae00',
            },
            bases=(models.Model,),
        ),
    ]
