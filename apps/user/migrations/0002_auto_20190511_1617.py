# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-05-11 16:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='verifycode',
            name='Email',
        ),
        migrations.AddField(
            model_name='verifycode',
            name='email',
            field=models.CharField(max_length=20, null=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='verifycode',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
    ]
