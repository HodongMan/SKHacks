# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-23 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sk', '0002_auto_20170823_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='Student',
            field=models.ManyToManyField(to='sk.Student'),
        ),
    ]