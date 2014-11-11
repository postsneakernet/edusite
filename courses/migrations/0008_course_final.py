# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_course_office_hours'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='final',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
