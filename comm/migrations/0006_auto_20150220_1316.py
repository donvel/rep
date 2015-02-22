# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0005_auto_20150219_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conclusion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(verbose_name='tre\u015b\u0107')),
                ('report', models.ForeignKey(to='comm.Report')),
            ],
            options={
                'verbose_name': 'wniosek',
                'verbose_name_plural': 'wnioski',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='branch',
            options={'verbose_name': 'filia', 'verbose_name_plural': 'filie'},
        ),
        migrations.AlterModelOptions(
            name='diocese',
            options={'verbose_name': 'diecezja', 'verbose_name_plural': 'diecezje'},
        ),
        migrations.AlterModelOptions(
            name='report',
            options={'verbose_name': 'sprawozdanie filialne', 'verbose_name_plural': 'sprawozdania filialne'},
        ),
        migrations.AlterUniqueTogether(
            name='report',
            unique_together=set([('branch', 'communion_day')]),
        ),
    ]
