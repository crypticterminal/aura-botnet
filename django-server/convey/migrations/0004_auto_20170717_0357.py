# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-17 03:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('convey', '0003_auto_20170717_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot_command',
            name='time_completed',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 17, 3, 57, 11, 375292, tzinfo=utc)),
        ),
    ]
