# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-08-18 21:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameCidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('slug', models.SlugField(verbose_name='Identificador')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('image', models.ImageField(blank=True, null=True, upload_to='cidades/images', verbose_name='Imagem')),
            ],
            options={
                'verbose_name_plural': 'Cidades',
                'verbose_name': 'Cidade',
            },
        ),
    ]
