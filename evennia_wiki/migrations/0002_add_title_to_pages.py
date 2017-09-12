# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 10:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evennia_wiki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='revision',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created on'),
        ),
    ]