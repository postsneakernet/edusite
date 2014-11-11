# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20141108_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='office_hours',
            field=models.CharField(max_length=200, default='monday 12:30 - 3:30'),
            preserve_default=False,
        ),
    ]
