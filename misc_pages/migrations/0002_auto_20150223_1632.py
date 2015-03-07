# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('misc_pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='miscpage',
            name='file_link',
        ),
        migrations.RemoveField(
            model_name='miscpage',
            name='is_file_link',
        ),
    ]
