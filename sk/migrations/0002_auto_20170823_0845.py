# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-23 08:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sk', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendence',
            old_name='Chapter_id',
            new_name='Chapter',
        ),
        migrations.RenameField(
            model_name='attendence',
            old_name='Lecture_id',
            new_name='Lecture',
        ),
        migrations.RenameField(
            model_name='attendence',
            old_name='Student_id',
            new_name='Student',
        ),
        migrations.RenameField(
            model_name='chapter',
            old_name='Lecture_id',
            new_name='Lecture',
        ),
        migrations.RenameField(
            model_name='lecture',
            old_name='Professor_id',
            new_name='Professor',
        ),
    ]
