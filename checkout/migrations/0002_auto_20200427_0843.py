# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-27 08:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='post_code',
            new_name='postcode',
        ),
    ]
