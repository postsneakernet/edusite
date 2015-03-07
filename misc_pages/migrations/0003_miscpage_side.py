# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('misc_pages', '0002_auto_20150223_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='miscpage',
            name='side',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
