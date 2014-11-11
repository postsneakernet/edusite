# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_course_final'),
        ('notifications', '0004_auto_20141109_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='course',
            field=models.ForeignKey(blank=True, null=True, to='courses.Course'),
            preserve_default=True,
        ),
    ]
