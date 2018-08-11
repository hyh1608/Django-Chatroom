# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-06 02:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0013_userprofile_friends'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-last_modify'], 'verbose_name': '帖子表', 'verbose_name_plural': '帖子表'},
        ),
        migrations.AddField(
            model_name='article',
            name='read_num',
            field=models.IntegerField(default=0),
        ),
    ]