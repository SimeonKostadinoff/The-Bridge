# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-14 22:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20160914_2247'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['timestamp']},
        ),
    ]
