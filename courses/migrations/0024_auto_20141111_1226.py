# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0023_project_groups'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='groups',
        ),
        migrations.AddField(
            model_name='project',
            name='group',
            field=models.CharField(null=True, max_length=200, blank=True, verbose_name='students'),
            preserve_default=True,
        ),
    ]
