# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import courses.models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_module_module_pdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignments',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('assignment_pdf', models.FileField(null=True, upload_to=courses.models.assignment_dir, blank=True)),
                ('misc_file', models.FileField(null=True, verbose_name='additional file', upload_to=courses.models.assignment_dir, blank=True)),
                ('body', models.TextField()),
                ('publish', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(to='courses.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='course',
            name='photo',
            field=models.ImageField(null=True, verbose_name='course photo', upload_to=courses.models.course_dir, blank=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='module_pdf',
            field=models.FileField(null=True, upload_to=courses.models.module_dir, blank=True),
        ),
    ]
