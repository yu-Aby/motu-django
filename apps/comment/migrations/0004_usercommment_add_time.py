# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-05-19 16:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_auto_20190519_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercommment',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
    ]
