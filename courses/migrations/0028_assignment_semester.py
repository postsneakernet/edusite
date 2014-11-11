# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0027_assignment_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='semester',
            field=models.CharField(default='fall 2010', max_length=200),
            preserve_default=False,
        ),
    ]
