# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0015_auto_20150220_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='number',
            field=models.IntegerField(default=0, verbose_name='liczba', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000)]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attendance',
            name='service',
            field=models.ForeignKey(default='', verbose_name='pos\u0142uga', to='comm.Service'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='diocese',
            name='name',
            field=models.CharField(help_text=b'np. "radomska"', max_length=100, verbose_name='nazwa'),
            preserve_default=True,
        ),
    ]
