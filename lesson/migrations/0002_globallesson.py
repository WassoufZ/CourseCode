# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-10-12 01:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scolarité', '0004_remove_subject_level'),
        ('lesson', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalLesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapiter', models.CharField(max_length=200)),
                ('lesson', models.CharField(max_length=200)),
                ('skill', models.CharField(max_length=200)),
                ('vacations', models.IntegerField()),
                ('link', models.URLField(blank=True, max_length=700, null=True)),
                ('remarques', models.TextField(blank=True, null=True)),
                ('order', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('state', models.BooleanField(default=False)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scolarité.Level')),
                ('levelsubject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scolarité.LevelSubject')),
            ],
        ),
    ]
