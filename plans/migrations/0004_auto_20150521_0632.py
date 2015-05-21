# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0003_auto_20150521_0618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fbuser',
            old_name='avator',
            new_name='avatar',
        ),
    ]
