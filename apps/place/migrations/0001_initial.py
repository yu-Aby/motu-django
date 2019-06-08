# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-05-15 12:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='城市名')),
                ('code', models.CharField(max_length=300, verbose_name='城市名code')),
            ],
            options={
                'verbose_name': '城市',
                'verbose_name_plural': '城市',
            },
        ),
        migrations.CreateModel(
            name='Tours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='景点名')),
                ('desc', models.CharField(max_length=300, verbose_name='描述')),
                ('place', models.CharField(max_length=300, verbose_name='地址')),
                ('img', models.CharField(max_length=300, verbose_name='图片')),
                ('time', models.CharField(blank=True, max_length=300, null=True, verbose_name='开放时间')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='门票价格')),
                ('detail_desc', models.TextField(blank=True, null=True, verbose_name='详细描述')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.City', verbose_name='所属城市')),
            ],
            options={
                'verbose_name': '景点',
                'verbose_name_plural': '景点',
            },
        ),
    ]
