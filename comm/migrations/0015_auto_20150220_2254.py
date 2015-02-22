# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0014_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('communion_day', models.ForeignKey(verbose_name='Dzie\u0144 Wsp\xf3lnoty', to='comm.CommunionDay')),
                ('diocese', models.ForeignKey(verbose_name='diecezja', to='comm.Diocese')),
            ],
            options={
                'verbose_name': 'obecno\u015b\u0107',
                'verbose_name_plural': 'obecno\u015bci',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='diocese',
            name='arch',
            field=models.BooleanField(default=False, verbose_name='archi'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='diocese',
            name='name',
            field=models.CharField(help_text=b'np. "siedlecka"', max_length=100, verbose_name='nazwa'),
            preserve_default=True,
        ),
    ]
