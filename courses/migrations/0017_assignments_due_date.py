# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0016_auto_20141110_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignments',
            name='due_date',
            field=models.DateTimeField(default=datetime.date(2014, 11, 10)),
            preserve_default=False,
        ),
    ]
