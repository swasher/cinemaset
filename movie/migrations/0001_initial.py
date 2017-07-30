# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-30 12:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmdbid', models.PositiveIntegerField(unique=True)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmdbid', models.PositiveIntegerField()),
                ('notice', models.TextField(blank=True, verbose_name='Заметка пользователя')),
                ('like', models.BooleanField(default=False, verbose_name='Лайк')),
                ('dislike', models.BooleanField(default=False, verbose_name='Дизлайк')),
                ('favorite', models.BooleanField(default=False, verbose_name='Любимый фильм')),
                ('watched', models.BooleanField(default=False, verbose_name='Просмотрено')),
                ('planned', models.BooleanField(default=False, verbose_name='Буду смотреть')),
                ('title', models.CharField(blank=True, max_length=128, verbose_name='Название на русском')),
                ('original_title', models.CharField(blank=True, max_length=128, verbose_name='Название на языке оригинала')),
                ('year', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Год выпуска')),
                ('overview', models.TextField(blank=True)),
                ('poster', models.CharField(blank=True, max_length=128, verbose_name="часть url'a для постера")),
                ('runtime', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Продолжительность в минутах')),
                ('imdbid', models.CharField(blank=True, max_length=16, verbose_name='id на imdb')),
                ('countries', models.ManyToManyField(to='movie.Country')),
                ('genres', models.ManyToManyField(to='movie.Genre')),
            ],
            options={
                'verbose_name_plural': 'Фильмы',
                'verbose_name': 'Фильм',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmdbid', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=30)),
                ('face', models.CharField(blank=True, max_length=128, verbose_name="часть url'a для постера")),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Фильмы',
                'verbose_name': 'Фильм',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('movie', models.ManyToManyField(blank=True, to='movie.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Списки',
                'verbose_name': 'Список',
            },
        ),
        migrations.AddField(
            model_name='movie',
            name='persons',
            field=models.ManyToManyField(to='movie.Person'),
        ),
        migrations.AddField(
            model_name='movie',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='person',
            unique_together=set([('tmdbid', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='movie',
            unique_together=set([('tmdbid', 'user')]),
        ),
    ]
