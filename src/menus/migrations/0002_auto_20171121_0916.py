# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-21 09:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='content',
            new_name='contents',
        ),
    ]