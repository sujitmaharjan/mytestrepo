# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 17:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('spiders', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CharField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('value', models.CharField(max_length=255, verbose_name='Name')),
                ('source_url', models.TextField(max_length=255, verbose_name='url')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IntegerField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('value', models.IntegerField(verbose_name='Value')),
                ('source_url', models.TextField(max_length=255, verbose_name='url')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='account',
            name='description',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account_description', to='leads.CharField'),
        ),
        migrations.AddField(
            model_name='account',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_name', to='leads.CharField'),
        ),
        migrations.AddField(
            model_name='account',
            name='spider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spiders.Spider'),
        ),
    ]
