# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-15 20:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DriverTest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='answer1',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='answer2',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='answer3',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='answer4',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.AddField(
            model_name='answer',
            name='answer',
            field=models.CharField(blank=True, max_length=100, verbose_name='\u0412\u0430\u0440\u0438\u0430\u043d\u0442 \u043e\u0442\u0432\u0435\u0442\u0430'),
        ),
        migrations.AddField(
            model_name='answer',
            name='true_or_false',
            field=models.CharField(choices=[('\u0412\u0435\u0440\u043d\u044b\u0439', True), ('\u041d\u0435\u0432\u0435\u0440\u043d\u044b\u0439', False)], default=False, max_length=5, verbose_name='\u0412\u0435\u0440\u043d\u044b\u0439 \u043e\u0442\u0432\u0435\u0442?'),
        ),
        migrations.AddField(
            model_name='question',
            name='answer1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question1', to='DriverTest.Answer', verbose_name='\u041e\u0442\u0432\u0435\u0442'),
        ),
        migrations.AddField(
            model_name='question',
            name='answer2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question2', to='DriverTest.Answer', verbose_name='\u041e\u0442\u0432\u0435\u0442'),
        ),
        migrations.AddField(
            model_name='question',
            name='answer3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question3', to='DriverTest.Answer', verbose_name='\u041e\u0442\u0432\u0435\u0442'),
        ),
        migrations.AddField(
            model_name='question',
            name='answer4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question4', to='DriverTest.Answer', verbose_name='\u041e\u0442\u0432\u0435\u0442'),
        ),
    ]