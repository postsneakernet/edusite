# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_details', '0007_detail_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='photo',
            field=models.ImageField(null=True, blank=True, upload_to='site_details'),
        ),
    ]
