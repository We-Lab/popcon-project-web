# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-08 03:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_movie_star_average'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boxofficemovie',
            old_name='created_date',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='boxofficemovie',
            old_name='modified_date',
            new_name='modified',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created_date',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='modified_date',
            new_name='modified',
        ),
        migrations.RenameField(
            model_name='commentlike',
            old_name='created_date',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='commentlike',
            old_name='modified_date',
            new_name='modified',
        ),
        migrations.RenameField(
            model_name='famouslike',
            old_name='created_date',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='famouslike',
            old_name='modified_date',
            new_name='modified',
        ),
        migrations.RenameField(
            model_name='famousline',
            old_name='modified_date',
            new_name='modified',
        ),
        migrations.RenameField(
            model_name='magazine',
            old_name='created_date',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='magazine',
            old_name='modified_date',
            new_name='modified',
        ),
        migrations.RemoveField(
            model_name='famousline',
            name='created_date',
        ),
        migrations.AddField(
            model_name='famousline',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]