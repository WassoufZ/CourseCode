# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-10-13 22:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scolarité', '0005_subject_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='level',
        ),
    ]
