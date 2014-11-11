# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import courses.models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0020_auto_20141110_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('semester', models.CharField(max_length=200)),
                ('student', models.BooleanField(verbose_name='Student Project', default=True)),
                ('due_date', models.DateTimeField(null=True, blank=True)),
                ('project_pdf', models.FileField(null=True, upload_to=courses.models.project_dir, blank=True)),
                ('misc_file', models.FileField(null=True, verbose_name='additional file', upload_to=courses.models.project_dir, blank=True)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(to='courses.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to=courses.models.file_dir),
        ),
    ]
