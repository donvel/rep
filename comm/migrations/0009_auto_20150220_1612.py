# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0008_customtext'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customtext',
            options={'verbose_name': 'pole tekstowe', 'verbose_name_plural': 'pola tekstowe'},
        ),
        migrations.AlterModelOptions(
            name='customtextconfig',
            options={'verbose_name': 'typ pola', 'verbose_name_plural': 'typy p\xf3l'},
        ),
        migrations.RemoveField(
            model_name='customtextconfig',
            name='always_present',
        ),
        migrations.AddField(
            model_name='customtextconfig',
            name='obligatory',
            field=models.BooleanField(default=False, help_text='Punktu obowi\u0105zkowe pojawi\u0105 si\u0119 w ka\u017cdym sprawozdaniu.', verbose_name='obowi\u0105zkowy'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customtext',
            name='config',
            field=models.ForeignKey(verbose_name='typ', to='comm.CustomTextConfig'),
            preserve_default=True,
        ),
    ]
