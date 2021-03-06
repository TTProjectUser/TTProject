# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 09:41
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('started', models.TextField(default=datetime.datetime(2016, 10, 21, 9, 41, 54, 328352, tzinfo=utc))),
                ('ended', models.DateTimeField()),
                ('last_modification', models.DateTimeField(blank=True, null=True)),
                ('all_day', models.BooleanField(default=False)),
                ('comment', models.CharField(max_length=300)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
