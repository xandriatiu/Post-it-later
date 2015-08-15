# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('queue', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('minimum_posts', models.IntegerField()),
                ('reward', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Redeem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('achievement', models.ForeignKey(to='users.Achievement')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coins', models.IntegerField(default=0)),
                ('bots', models.ManyToManyField(to='queue.Bots')),
                ('user', models.ForeignKey(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
