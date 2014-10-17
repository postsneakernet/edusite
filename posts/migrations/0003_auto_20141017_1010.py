# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20141017_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='unique name'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
