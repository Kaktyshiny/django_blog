# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-13 20:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_auto_20171213_2026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='user_name',
        ),
        migrations.AddField(
            model_name='articles',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
