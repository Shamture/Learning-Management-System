# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-28 11:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0005_auto_20180527_0958'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Grades',
            new_name='Grade',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='comments',
        ),
        migrations.AddField(
            model_name='quiz',
            name='comment',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classroom.Comments'),
        ),
    ]
