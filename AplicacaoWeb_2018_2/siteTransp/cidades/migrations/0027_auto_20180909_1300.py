# Generated by Django 2.1.1 on 2018-09-09 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cidades', '0026_auto_20180908_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='cidade',
        ),
        migrations.DeleteModel(
            name='Projeto',
        ),
    ]
