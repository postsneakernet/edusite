# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='body',
            field=models.TextField(max_length=130),
        ),
        migrations.AlterField(
            model_name='notification',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
