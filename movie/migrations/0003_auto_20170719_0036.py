# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-19 00:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20170718_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='heart',
            field=models.BooleanField(default=False, verbose_name='Любимый фильм'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='dislike',
            field=models.BooleanField(default=False, verbose_name='Дизлайк'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='like',
            field=models.BooleanField(default=False, verbose_name='Лайк'),
        ),
    ]