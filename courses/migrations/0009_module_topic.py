# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_course_final'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='topic',
            field=models.CharField(max_length=200, default='Java Security'),
            preserve_default=False,
        ),
    ]
