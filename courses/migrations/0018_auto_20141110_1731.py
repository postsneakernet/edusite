# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import courses.models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0017_assignments_due_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('due_date', models.DateTimeField()),
                ('assignment_pdf', models.FileField(upload_to=courses.models.assignment_dir, blank=True, null=True)),
                ('misc_file', models.FileField(verbose_name='additional file', upload_to=courses.models.assignment_dir, blank=True, null=True)),
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
        migrations.RemoveField(
            model_name='assignments',
            name='course',
        ),
        migrations.DeleteModel(
            name='Assignments',
        ),
    ]
