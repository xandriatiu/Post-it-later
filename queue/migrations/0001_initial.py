# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('djcelery', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bots',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(default=1, editable=False, db_index=True)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to=b'bots')),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('social_media', models.CharField(max_length=255, choices=[(b'smtp', b'Email'), (b'facebook', b'Facebook'), (b'twitter', b'Twitter'), (b'plurk', b'Plurk')])),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['order'],
                'abstract': False,
                'verbose_name_plural': 'Bots',
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('bot', models.ForeignKey(to='queue.Bots')),
                ('task', models.ForeignKey(blank=True, to='djcelery.PeriodicTask', null=True)),
                ('user', models.ForeignKey(related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
