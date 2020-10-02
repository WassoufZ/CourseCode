# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-09-30 12:51
from __future__ import unicode_literals

from django.db import migrations, models
import users.models.user_manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('username', models.CharField(max_length=40, null=True)),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('user_type', models.CharField(blank=True, max_length=30, verbose_name='type')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_confirmed', models.BooleanField(default=True, verbose_name='inscription confirmée')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', users.models.user_manager.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Pays')),
                ('country_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='Code Pays')),
                ('state_name', models.CharField(max_length=100, verbose_name='Wilaya')),
                ('state_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='Code Wilaya')),
                ('street_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Rue')),
                ('postal_code', models.IntegerField(null=True)),
            ],
        ),
    ]
