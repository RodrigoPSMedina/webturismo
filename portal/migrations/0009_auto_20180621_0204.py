# Generated by Django 2.0.5 on 2018-06-21 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_auto_20180621_0158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='estado',
        ),
        migrations.AlterField(
            model_name='news',
            name='legenda',
            field=models.CharField(help_text='Digite a legenda da foto', max_length=255),
        ),
    ]