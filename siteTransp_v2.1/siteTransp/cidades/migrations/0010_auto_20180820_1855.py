# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-08-20 18:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cidades', '0009_auto_20180820_1842'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cidade',
            options={'ordering': ['nameCidade'], 'verbose_name': 'Cidade', 'verbose_name_plural': 'Cidades'},
        ),
        migrations.AlterModelOptions(
            name='orgao',
            options={'ordering': ['nameOrgao'], 'verbose_name': 'Orgao', 'verbose_name_plural': 'Orgaos'},
        ),
    ]