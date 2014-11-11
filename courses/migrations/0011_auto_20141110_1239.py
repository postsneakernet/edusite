# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_course_grades'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='grades',
            field=models.CharField(max_length=200, blank=True, null=True),
        ),
    ]
