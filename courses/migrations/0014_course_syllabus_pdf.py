# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import courses.models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_auto_20141110_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='syllabus_pdf',
            field=models.FileField(null=True, blank=True, upload_to=courses.models.course_dir),
            preserve_default=True,
        ),
    ]
