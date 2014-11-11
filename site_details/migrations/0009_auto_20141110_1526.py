# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_details', '0008_auto_20141110_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='lab_photo',
            field=models.ImageField(null=True, upload_to='site_details', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='detail',
            name='photo',
            field=models.ImageField(null=True, verbose_name='instructor photo', upload_to='site_details', blank=True),
        ),
    ]
