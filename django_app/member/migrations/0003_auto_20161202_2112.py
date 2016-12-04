# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 12:12
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20161201_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]