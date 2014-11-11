# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_details', '0003_auto_20141109_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='lab_name',
            field=models.CharField(max_length=250, default='FGCU Robotics Lab'),
            preserve_default=False,
        ),
    ]
