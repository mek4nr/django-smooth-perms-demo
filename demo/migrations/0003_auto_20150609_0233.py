# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20150609_0221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='continentpermission',
            name='can_add_continent',
        ),
        migrations.RemoveField(
            model_name='continentpermission',
            name='can_delete_continent',
        ),
        migrations.AddField(
            model_name='continentpermission',
            name='can_change_continent',
            field=models.BooleanField(default=False, verbose_name='can change continent'),
        ),
    ]
