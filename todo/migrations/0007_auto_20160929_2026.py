# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 20:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_auto_20160929_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='list_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='todo.List'),
        ),
    ]