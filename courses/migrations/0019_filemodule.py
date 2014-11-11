# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import courses.models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0018_auto_20141110_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileModule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('m_file', models.FileField(blank=True, upload_to=courses.models.module_dir, null=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('module', models.ForeignKey(to='courses.Module')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
