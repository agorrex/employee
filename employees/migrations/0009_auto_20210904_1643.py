# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2021-09-04 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0008_auto_20210904_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True),
        ),
    ]
