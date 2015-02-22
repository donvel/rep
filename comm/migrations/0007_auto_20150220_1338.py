# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0006_auto_20150220_1316'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomTextConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='nazwa')),
                ('always_present', models.BooleanField(default=False, help_text='Punkty sta\u0142e pojawiaj\u0105 si\u0119 w ka\u017cdym sprawozdaniu.', verbose_name='sta\u0142y punkt')),
            ],
            options={
                'verbose_name': 'w\u0142asne pole',
                'verbose_name_plural': 'w\u0142asne pola',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='communionday',
            name='name',
            field=models.CharField(help_text=b'kr\xc3\xb3tsza ni\xc5\xbc temat :-}', max_length=100, verbose_name='nazwa'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='communionday',
            name='topic',
            field=models.TextField(verbose_name='temat'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='conclusion',
            name='report',
            field=models.ForeignKey(verbose_name='sprawozdanie', to='comm.Report'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='diocese',
            name='branch',
            field=models.ForeignKey(verbose_name='filia', to='comm.Branch'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='report',
            name='branch',
            field=models.ForeignKey(verbose_name='filia', to='comm.Branch'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='report',
            name='communion_day',
            field=models.ForeignKey(verbose_name='Dzie\u0144 Wsp\xf3lnoty', to='comm.CommunionDay'),
            preserve_default=True,
        ),
    ]
