# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-16 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('total', models.IntegerField()),
                ('email', models.CharField(max_length=30)),
            ],
        ),
    ]
