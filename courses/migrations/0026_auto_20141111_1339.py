# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0025_project_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='archive',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(verbose_name='unique name', max_length=200, default=datetime.date(2014, 11, 11), unique=True),
            preserve_default=False,
        ),
    ]
