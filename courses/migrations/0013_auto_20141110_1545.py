# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import courses.models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_course_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='photo',
            field=models.ImageField(blank=True, upload_to=courses.models.course_dir, null=True),
        ),
    ]
