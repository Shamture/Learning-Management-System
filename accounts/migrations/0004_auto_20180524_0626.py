# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-24 06:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180523_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('System Admin', 'AD'), ('Admin', 'LA'), ('Instructor', 'IN'), ('Teaching Assistant', 'TA'), ('Student', 'Student')], max_length=2),
        ),
    ]
