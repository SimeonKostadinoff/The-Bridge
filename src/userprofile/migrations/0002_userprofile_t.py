# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-02 16:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='t',
            field=models.TextField(default='2'),
        ),
    ]