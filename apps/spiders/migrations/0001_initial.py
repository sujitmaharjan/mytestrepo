# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 17:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('verticals', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.TextField(blank=True, max_length=255, verbose_name='Description')),
                ('url', models.CharField(max_length=255, verbose_name='Base URL of the spider')),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approved_spiders', to=settings.AUTH_USER_MODEL)),
                ('suggested_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suggested_spiders', to=settings.AUTH_USER_MODEL)),
                ('vertical', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spiders', to='verticals.Vertical')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
