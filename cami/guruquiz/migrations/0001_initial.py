# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 22:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yt_username', models.CharField(max_length=200)),
                ('yt_display_name', models.CharField(max_length=200)),
                ('yt_id', models.CharField(max_length=200)),
                ('yt_home_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BloggerToQuiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_modified', models.DateTimeField(verbose_name='last modified at')),
                ('blogger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guruquiz.Blogger')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProductToVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_modified', models.DateTimeField(verbose_name='last modified at')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guruquiz.Blogger')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=200)),
                ('question_text', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('transcript', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('blogger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guruquiz.Blogger')),
            ],
        ),
        migrations.AddField(
            model_name='producttovideo',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guruquiz.Video'),
        ),
        migrations.AddField(
            model_name='bloggertoquiz',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guruquiz.Quiz'),
        ),
    ]