# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_details', '0009_auto_20141110_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='research_photo',
            field=models.ImageField(null=True, blank=True, upload_to='site_details'),
            preserve_default=True,
        ),
    ]
