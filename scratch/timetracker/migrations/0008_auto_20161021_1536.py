# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 13:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('timetracker', '0007_auto_20161021_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 21, 13, 36, 21, 699892, tzinfo=utc)),
        ),
    ]
