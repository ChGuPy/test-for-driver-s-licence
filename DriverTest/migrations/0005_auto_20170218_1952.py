# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-18 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DriverTest', '0004_auto_20170215_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.TextField(blank=True, max_length=100, verbose_name='\u0412\u0430\u0440\u0438\u0430\u043d\u0442 \u043e\u0442\u0432\u0435\u0442\u0430'),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.TextField(max_length=300, verbose_name='\u0412\u043e\u043f\u0440\u043e\u0441'),
        ),
    ]
