# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_entry_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='course',
            field=models.ForeignKey(null=True, blank=True, to='courses.Course'),
        ),
    ]
