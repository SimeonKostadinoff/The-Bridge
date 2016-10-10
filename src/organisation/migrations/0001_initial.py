# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-10 11:59
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import organisation.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('locations', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('Education', 'Education'), ('Environment', 'Environment'), ('Public Services', 'Public Services')], max_length=255)),
                ('phone_number', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')])),
                ('email_organisation', models.EmailField(max_length=254)),
                ('website', models.URLField(max_length=255)),
                ('front_picture', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='organisation/profile')),
                ('cover_picture', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='organisation/cover')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0, validators=[organisation.models.validate_rating])),
                ('text', models.TextField(blank=True)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organisation.Organisation')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
