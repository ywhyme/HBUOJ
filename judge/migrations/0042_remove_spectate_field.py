# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-18 19:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0041_virtual_contest_participation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contestparticipation',
            name='spectate',
        ),
    ]
