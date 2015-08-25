# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_auto_20150609_0233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='continentpermission',
            name='can_change_continent',
        ),
        migrations.AddField(
            model_name='continentpermission',
            name='can_change_country',
            field=models.BooleanField(verbose_name='can change country', default=False),
        ),
    ]
