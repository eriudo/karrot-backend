# -*- coding: utf-8 -*-
# Generated by Django 1.9a1 on 2015-10-03 12:04
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yunity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapitem',
            name='contacts',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='mapitem',
            name='metadata',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]
