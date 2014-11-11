# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_prefix'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='prefix',
            field=models.CharField(verbose_name='course abbreviation', max_length=20, default='fgcu'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='prefix',
            field=models.CharField(verbose_name='course abbreviation', max_length=20),
        ),
    ]
