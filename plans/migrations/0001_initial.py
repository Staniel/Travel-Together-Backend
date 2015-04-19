# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FBUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fbid', models.CharField(max_length=20)),
                ('access_token', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='JoinedPlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('destination', models.CharField(max_length=200)),
                ('limit', models.IntegerField()),
                ('depart_time', models.DateTimeField()),
                ('length', models.IntegerField()),
                ('visible_type', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
                ('holder', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PrivatePlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('accessible_plan', models.ForeignKey(to='plans.Plan')),
                ('accessible_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='joinedplan',
            name='joined_plan',
            field=models.ForeignKey(to='plans.Plan'),
        ),
        migrations.AddField(
            model_name='joinedplan',
            name='joined_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
