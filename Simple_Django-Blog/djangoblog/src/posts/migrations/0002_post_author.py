# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-11 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default=-1.0, max_length=120),
            preserve_default=False,
        ),
    ]