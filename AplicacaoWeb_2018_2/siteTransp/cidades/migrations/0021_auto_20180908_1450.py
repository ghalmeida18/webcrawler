# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-08 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cidades', '0020_auto_20180908_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='nameProjeto',
            field=models.TextField(max_length=100, unique=True, verbose_name='Projeto'),
        ),
    ]
