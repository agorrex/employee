# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2021-09-04 10:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_auto_20210904_1054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='name',
            new_name='full_name',
        ),
    ]
