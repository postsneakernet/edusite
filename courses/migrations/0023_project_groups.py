# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0022_auto_20141111_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='groups',
            field=models.CharField(blank=True, null=True, max_length=200),
            preserve_default=True,
        ),
    ]
