# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-15 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DriverTest', '0002_auto_20170215_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='true_or_false',
            field=models.BooleanField(choices=[(True, '\u0412\u0435\u0440\u043d\u044b\u0439'), (False, '\u041d\u0435\u0432\u0435\u0440\u043d\u044b\u0439')], default=False, max_length=5, verbose_name='\u0412\u0435\u0440\u043d\u044b\u0439 \u043e\u0442\u0432\u0435\u0442?'),
        ),
    ]
