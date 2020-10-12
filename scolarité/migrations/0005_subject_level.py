# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-10-12 22:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scolarité', '0004_remove_subject_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='level',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='scolarité.Level'),
            preserve_default=False,
        ),
    ]
