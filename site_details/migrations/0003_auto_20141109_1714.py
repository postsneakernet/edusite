# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_details', '0002_auto_20141103_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='email',
            field=models.EmailField(default='zalewski@fgcu.edu', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detail',
            name='office',
            field=models.CharField(default='Holmes Engineering 411', max_length=200),
            preserve_default=False,
        ),
    ]
