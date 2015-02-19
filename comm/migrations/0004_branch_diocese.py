# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0003_auto_20150219_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nazwa')),
            ],
            options={
                'verbose_name': 'Filia',
                'verbose_name_plural': 'Filie',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Diocese',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'nazwa')),
                ('branch', models.ForeignKey(to='comm.Branch')),
            ],
            options={
                'verbose_name': 'Filia',
                'verbose_name_plural': 'Filie',
            },
            bases=(models.Model,),
        ),
    ]
