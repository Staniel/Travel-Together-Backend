# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0002_fbuser_access_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='fbuser',
            name='avator',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='plan',
            name='visible_type',
            field=models.IntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='joinedplan',
            unique_together=set([('joined_user', 'joined_plan')]),
        ),
        migrations.AlterUniqueTogether(
            name='privateplan',
            unique_together=set([('accessible_user', 'accessible_plan')]),
        ),
    ]
