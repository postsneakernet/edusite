# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_details', '0006_auto_20141109_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
            preserve_default=True,
        ),
    ]
