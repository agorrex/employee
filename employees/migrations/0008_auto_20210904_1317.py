# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2021-09-04 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0007_myuser_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='image',
            field=models.TextField(default=''),
        ),
    ]
