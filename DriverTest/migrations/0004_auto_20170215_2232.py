# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-15 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DriverTest', '0003_auto_20170215_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=300, verbose_name='\u0412\u043e\u043f\u0440\u043e\u0441'),
        ),
    ]
