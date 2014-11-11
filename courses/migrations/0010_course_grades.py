# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_module_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='grades',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
