# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-02 12:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0016_auto_20180602_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='quiz',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='classroom.QuizOrAssignment'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='score',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
        ),
    ]
