# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-31 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='admins',
            field=models.ManyToManyField(blank=True, to='bbs.UserProfile', verbose_name='版主'),
        ),
    ]
