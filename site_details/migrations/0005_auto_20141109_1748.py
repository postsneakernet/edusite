# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_details', '0004_detail_lab_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='lab_room',
            field=models.CharField(max_length=200, default='Holmes Engineering 403'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='detail',
            name='email',
            field=models.EmailField(max_length=200),
        ),
        migrations.AlterField(
            model_name='detail',
            name='lab_name',
            field=models.CharField(max_length=200),
        ),
    ]
