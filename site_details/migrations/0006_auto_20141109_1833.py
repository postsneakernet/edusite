# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_details', '0005_auto_20141109_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='education',
            field=models.TextField(default='placeholder'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detail',
            name='employment',
            field=models.TextField(default='asdf'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detail',
            name='other_resume',
            field=models.TextField(default='asdf'),
            preserve_default=False,
        ),
    ]
