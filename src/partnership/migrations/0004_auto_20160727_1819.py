# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 18:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partnership', '0003_auto_20160727_1806'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pendingrequest',
            old_name='organization',
            new_name='organisation',
        ),
    ]