# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0026_auto_20141111_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='slug',
            field=models.SlugField(unique=True, max_length=200, verbose_name='unique name', default=datetime.date(2014, 11, 11)),
            preserve_default=False,
        ),
    ]
