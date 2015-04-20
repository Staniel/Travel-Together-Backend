# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fbuser',
            name='access_token',
            field=models.CharField(default=datetime.datetime(2015, 4, 20, 2, 8, 45, 921796, tzinfo=utc), max_length=500),
            preserve_default=False,
        ),
    ]
