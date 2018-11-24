# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empenho',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('Especie', models.CharField(db_column='Especie', max_length=25)),
                ('Orgao', models.CharField(db_column='Orgao', max_length=100)),
                ('Projeto', models.CharField(db_column='Projeto', max_length=100)),
                ('Elemento', models.CharField(db_column='Elemento', max_length=100)),
                ('Licitacao', models.CharField(db_column='Licitacao', max_length=50)),
                ('Processo', models.CharField(db_column='Processo', max_length=30)),
                ('Dataempenho', models.DateField(db_column='DataEmpenho')),
                ('Valor', models.DecimalField(db_column='Valor', decimal_places=2, max_digits=12, blank=True, null=True)),
                ('Empenho_Numero', models.IntegerField(db_column='Empenho_Numero')),
                ('Funcao', models.CharField(db_column='Funcao', max_length=100)),
                ('Subfuncao', models.CharField(db_column='SubFuncao', max_length=100)),
                ('Programa', models.CharField(db_column='Programa', max_length=100)),
                ('Destinacao', models.CharField(db_column='Destinacao', max_length=45)),
            ],
            options={
                'managed': False,
                'db_table': 'Empenho',
            },
        ),
        migrations.CreateModel(
            name='Favorecido',
            fields=[
                ('IdFavorecido', models.AutoField(db_column='IdFavorecido', serialize=False, primary_key=True)),
                ('CPF_CNPJ', models.CharField(db_column='CPF_CNPJ', max_length=20)),
                ('Nome', models.CharField(db_column='Nome', unique=True, max_length=100)),
                ('Cargo', models.CharField(db_column='Cargo', max_length=45, blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'Favorecido',
            },
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('Numero', models.IntegerField(db_column='Numero')),
                ('DataPagamento', models.DateField(db_column='DataPagamento')),
                ('ValorPagamento', models.DecimalField(db_column='ValorPagamento', decimal_places=2, max_digits=12, blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'Pagamento',
            },
        ),
    ]
