# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20141108_2338'),
        ('posts', '0004_auto_20141017_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='course',
            field=models.ForeignKey(null=True, to='courses.Course'),
            preserve_default=True,
        ),
    ]
