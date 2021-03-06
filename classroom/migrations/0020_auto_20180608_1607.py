# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-08 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0019_auto_20180608_1536'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='quiz',
            new_name='quiz_or_assignment',
        ),
        migrations.AlterField(
            model_name='grade',
            name='score',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Score is expressed in percentage', max_digits=100),
        ),
    ]
