# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import courses.models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_course_syllabus_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='module_pdf',
            field=models.FileField(null=True, upload_to=courses.models.course_dir, blank=True),
            preserve_default=True,
        ),
    ]
