# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_details', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detail',
            old_name='about_detail',
            new_name='about',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='about_brief',
        ),
        migrations.AddField(
            model_name='detail',
            name='lab',
            field=models.TextField(default='asdf'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detail',
            name='research',
            field=models.TextField(default='asdf'),
            preserve_default=False,
        ),
    ]
