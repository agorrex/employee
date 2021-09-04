# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2021-09-04 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='address',
            field=models.TextField(default=''),
        ),
        # migrations.AddField(
        #     model_name='myuser',
        #     name='image',
        #     field=models.BigIntegerField(default=None),
        # ),
        migrations.AddField(
            model_name='myuser',
            name='name',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='myuser',
            name='phone',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
