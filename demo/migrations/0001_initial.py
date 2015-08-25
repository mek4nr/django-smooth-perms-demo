# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created_at', models.DateTimeField(verbose_name='created at', auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('name', models.CharField(max_length=1000)),
                ('color', models.CharField(max_length=20)),
                ('owner', models.ForeignKey(blank=True, verbose_name='owner', related_name='owned_cars', null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CarPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('can_change', models.BooleanField(verbose_name='can edit', default=False)),
                ('can_advanced_settings', models.BooleanField(verbose_name='can change advanced settings', default=False)),
                ('can_delete', models.BooleanField(verbose_name='can delete', default=False)),
                ('can_change_permissions', models.BooleanField(verbose_name='can change permissions', default=False)),
                ('can_delete_permissions', models.BooleanField(verbose_name='can delete permissions', default=False)),
                ('can_view', models.BooleanField(verbose_name='view restricted', default=False)),
                ('car', models.ForeignKey(to='demo.Car')),
                ('group', models.ForeignKey(blank=True, verbose_name='group', null=True, to='auth.Group')),
                ('user', models.ForeignKey(blank=True, verbose_name='user', null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created_at', models.DateTimeField(verbose_name='created at', auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('name', models.CharField(max_length=1000)),
                ('color', models.CharField(max_length=20)),
                ('owner', models.ForeignKey(blank=True, verbose_name='owner', related_name='owned_continents', null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContinentPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('can_change', models.BooleanField(verbose_name='can edit', default=False)),
                ('can_advanced_settings', models.BooleanField(verbose_name='can change advanced settings', default=False)),
                ('can_delete', models.BooleanField(verbose_name='can delete', default=False)),
                ('can_change_permissions', models.BooleanField(verbose_name='can change permissions', default=False)),
                ('can_delete_permissions', models.BooleanField(verbose_name='can delete permissions', default=False)),
                ('can_view', models.BooleanField(verbose_name='view restricted', default=False)),
                ('can_delete_continent', models.BooleanField(verbose_name='can delete continent', default=False)),
                ('can_add_continent', models.BooleanField(verbose_name='can add continent', default=False)),
                ('continent', models.ForeignKey(to='demo.Continent')),
                ('group', models.ForeignKey(blank=True, verbose_name='group', null=True, to='auth.Group')),
                ('user', models.ForeignKey(blank=True, verbose_name='user', null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created_at', models.DateTimeField(verbose_name='created at', auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('name', models.CharField(max_length=1000)),
                ('citizen', models.PositiveIntegerField()),
                ('continent', models.ForeignKey(to='demo.Continent')),
                ('owner', models.ForeignKey(blank=True, verbose_name='owner', related_name='owned_countrys', null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CountryPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('can_change', models.BooleanField(verbose_name='can edit', default=False)),
                ('can_advanced_settings', models.BooleanField(verbose_name='can change advanced settings', default=False)),
                ('can_delete', models.BooleanField(verbose_name='can delete', default=False)),
                ('can_change_permissions', models.BooleanField(verbose_name='can change permissions', default=False)),
                ('can_delete_permissions', models.BooleanField(verbose_name='can delete permissions', default=False)),
                ('can_view', models.BooleanField(verbose_name='view restricted', default=False)),
                ('country', models.ForeignKey(to='demo.Country')),
                ('group', models.ForeignKey(blank=True, verbose_name='group', null=True, to='auth.Group')),
                ('user', models.ForeignKey(blank=True, verbose_name='user', null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
