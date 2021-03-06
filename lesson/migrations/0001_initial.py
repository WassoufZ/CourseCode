# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-10-11 21:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import lesson.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('scolarité', '0004_remove_subject_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('document', models.FileField(upload_to='', validators=[lesson.validators.validate_document_extension])),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.FileField(upload_to='', validators=[lesson.validators.validate_image_extension])),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
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
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scolarité.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.URLField()),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lesson.Lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('video', models.FileField(upload_to='', validators=[lesson.validators.validate_file_extension])),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lesson.Lesson')),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='lesson',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='lesson.Lesson'),
        ),
        migrations.AddField(
            model_name='document',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lesson.Lesson'),
        ),
    ]
