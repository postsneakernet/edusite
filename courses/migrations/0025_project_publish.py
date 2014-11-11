# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0024_auto_20141111_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='publish',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
