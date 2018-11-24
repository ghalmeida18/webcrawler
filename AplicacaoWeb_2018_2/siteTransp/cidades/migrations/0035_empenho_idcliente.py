# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-10 04:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cidades', '0034_auto_20180910_0441'),
    ]

    operations = [
        migrations.AddField(
            model_name='empenho',
            name='idCliente',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cidades.Cidade', verbose_name='empIdCliente'),
            preserve_default=False,
        ),
    ]
