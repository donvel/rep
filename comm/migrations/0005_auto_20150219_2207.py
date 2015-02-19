# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0004_branch_diocese'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('branch', models.ForeignKey(to='comm.Branch')),
                ('communion_day', models.ForeignKey(to='comm.CommunionDay')),
            ],
            options={
                'verbose_name': 'Sprawozdanie filialne',
                'verbose_name_plural': 'Sprawozdania filialne',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='diocese',
            options={'verbose_name': 'Diecezja', 'verbose_name_plural': 'Diecezje'},
        ),
    ]
