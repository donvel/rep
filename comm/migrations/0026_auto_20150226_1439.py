# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0025_auto_20150224_1330'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branch',
            options={'ordering': ['name'], 'verbose_name': 'filia', 'verbose_name_plural': 'filie'},
        ),
        migrations.AlterModelOptions(
            name='customtextconfig',
            options={'ordering': ['-display_priority'], 'verbose_name': 'typ pola', 'verbose_name_plural': 'typy p\xf3l'},
        ),
        migrations.AlterModelOptions(
            name='diocese',
            options={'ordering': ['name'], 'verbose_name': 'diecezja', 'verbose_name_plural': 'diecezje'},
        ),
        migrations.AlterField(
            model_name='service',
            name='full_name',
            field=models.CharField(unique=True, max_length=100, verbose_name='pe\u0142na nazwa'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='customtext',
            unique_together=set([('report', 'config')]),
        ),
    ]
