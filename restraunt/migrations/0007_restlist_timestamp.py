# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-20 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restraunt', '0006_remove_restlist_int_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='restlist',
            name='timestamp',
            field=models.DateTimeField(null=True),
        ),
    ]