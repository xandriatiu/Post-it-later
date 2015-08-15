# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('queue', '0001_initial'),
        ('userprofile', '0002_auto_20150815_0631'),
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
                ('achievement', models.ForeignKey(to='userprofile.Achievement')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='avatar_url',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='bots',
            field=models.ManyToManyField(to='queue.Bots'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='coins',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(related_name='profile', default='', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
