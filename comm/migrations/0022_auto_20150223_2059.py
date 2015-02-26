# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0021_auto_20150223_2038'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branch',
            options={'ordering': ['-name'], 'verbose_name': 'filia', 'verbose_name_plural': 'filie'},
        ),
        migrations.AlterModelOptions(
            name='communionday',
            options={'ordering': ['-date'], 'verbose_name': 'Dzie\u0144 Wsp\xf3lnoty', 'verbose_name_plural': 'Dni Wsp\xf3lnoty'},
        ),
        migrations.AlterModelOptions(
            name='customtextconfig',
            options={'ordering': ['-name'], 'verbose_name': 'typ pola', 'verbose_name_plural': 'typy p\xf3l'},
        ),
        migrations.AlterModelOptions(
            name='diocese',
            options={'ordering': ['-name'], 'verbose_name': 'diecezja', 'verbose_name_plural': 'diecezje'},
        ),
        migrations.AlterField(
            model_name='branch',
            name='name',
            field=models.CharField(unique=True, max_length=100, verbose_name='nazwa'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customtextconfig',
            name='name',
            field=models.CharField(unique=True, max_length=100, verbose_name='nazwa'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='diocese',
            name='name',
            field=models.CharField(help_text=b'np. "radomska"', unique=True, max_length=100, verbose_name='nazwa'),
            preserve_default=True,
        ),
    ]
