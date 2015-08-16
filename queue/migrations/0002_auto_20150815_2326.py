# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('queue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bots',
            name='social_media',
            field=models.CharField(max_length=255, choices=[(b'smtp', b'Email'), (b'plurk', b'Plurk'), (b'twitter', b'Twitter'), (b'facebook', b'Facebook')]),
        ),
    ]
