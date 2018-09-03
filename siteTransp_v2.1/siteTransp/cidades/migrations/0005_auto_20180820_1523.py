# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-08-20 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cidades', '0004_orgao_cidade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orgao',
            name='cidade',
        ),
        migrations.AlterField(
            model_name='cidade',
            name='about',
            field=models.TextField(blank=True, default=1, verbose_name='Sobre a cidade'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cidade',
            name='description',
            field=models.TextField(blank=True, default=1, verbose_name='Descrição'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orgao',
            name='description',
            field=models.TextField(blank=True, default=1, verbose_name='Descrição'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projeto',
            name='description',
            field=models.TextField(blank=True, default=1, verbose_name='Descrição'),
            preserve_default=False,
        ),
    ]