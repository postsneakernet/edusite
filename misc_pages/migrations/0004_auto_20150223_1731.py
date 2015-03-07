# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('misc_pages', '0003_miscpage_side'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='miscpage',
            options={'ordering': ['modified']},
        ),
    ]
