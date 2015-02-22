# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0016_auto_20150220_2301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='communion_day',
        ),
        migrations.AddField(
            model_name='attendance',
            name='report',
            field=models.ForeignKey(default='', verbose_name='sprawozdanie', to='comm.Report'),
            preserve_default=False,
        ),
    ]
