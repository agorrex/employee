# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2021-09-04 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_auto_20210904_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_employee',
            field=models.BooleanField(default=True),
        ),
    ]
