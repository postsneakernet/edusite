# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0021_auto_20141111_1103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='student',
        ),
        migrations.AddField(
            model_name='project',
            name='requirement',
            field=models.BooleanField(default=False, verbose_name='Project requirement submission'),
            preserve_default=True,
        ),
    ]
