# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('misc_pages', '0004_auto_20150223_1731'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='miscpage',
            options={'ordering': ['-modified']},
        ),
    ]
