# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-05-19 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_usercommment_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercommment',
            name='content',
            field=models.TextField(default='', verbose_name='评论内容'),
        ),
    ]