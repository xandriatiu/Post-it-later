# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('avatar_url', models.ImageField(max_length=200, upload_to=b'')),
                ('date_created', models.DateTimeField(verbose_name=b'Date Created')),
            ],
        ),
    ]
