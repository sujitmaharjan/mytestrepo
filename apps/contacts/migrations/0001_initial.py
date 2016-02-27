# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 17:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Spider Name')),
                ('description', models.TextField(blank=True, max_length=255, verbose_name='Spider Name')),
                ('url', models.CharField(max_length=255, verbose_name='Main URL of the spider')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
