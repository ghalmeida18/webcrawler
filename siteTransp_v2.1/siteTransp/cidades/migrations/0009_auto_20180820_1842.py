# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-08-20 18:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cidades', '0008_auto_20180820_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='orgao',
        ),
        migrations.DeleteModel(
            name='Projeto',
        ),
    ]
