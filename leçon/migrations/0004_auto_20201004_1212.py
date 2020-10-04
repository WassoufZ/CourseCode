# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-10-04 11:12
from __future__ import unicode_literals

from django.db import migrations, models
import leçon.validators


class Migration(migrations.Migration):

    dependencies = [
        ('leçon', '0003_auto_20201003_1638'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image',
            new_name='thumbnail',
        ),
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='', validators=[leçon.validators.validate_document_extension]),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='', validators=[leçon.validators.validate_file_extension]),
        ),
    ]
