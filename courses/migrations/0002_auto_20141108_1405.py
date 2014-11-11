# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='created',
            field=models.DateTimeField(default=datetime.date(2014, 11, 8), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='modified',
            field=models.DateTimeField(default=datetime.date(2014, 11, 8), auto_now=True),
            preserve_default=False,
        ),
    ]
