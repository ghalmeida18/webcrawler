# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-08-20 15:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cidades', '0003_orgao_projeto'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgao',
            name='cidade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cidades.Cidade'),
            preserve_default=False,
        ),
    ]
