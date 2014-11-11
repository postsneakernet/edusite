# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_module_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='prefix',
            field=models.CharField(max_length=20, verbose_name='course prefix', default='fgcu'),
            preserve_default=False,
        ),
    ]
