# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import misc_pages.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('file', models.FileField(upload_to=misc_pages.models.file_dir)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MiscPage',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('is_external_link', models.BooleanField(default=False)),
                ('external_link', models.CharField(max_length=1000, null=True, blank=True)),
                ('is_file_link', models.BooleanField(default=False)),
                ('file_link', models.CharField(max_length=1000, null=True, blank=True)),
                ('misc_file', models.FileField(upload_to=misc_pages.models.misc_dir, null=True, blank=True)),
                ('body', models.TextField(null=True, blank=True)),
                ('publish', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['title'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='file',
            name='misc_page',
            field=models.ForeignKey(to='misc_pages.MiscPage'),
            preserve_default=True,
        ),
    ]
