# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0019_customtextconfig_use_in_report'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['-display_prioirity'], 'verbose_name': 'pos\u0142uga', 'verbose_name_plural': 'pos\u0142ugi'},
        ),
        migrations.AddField(
            model_name='service',
            name='display_prioirity',
            field=models.IntegerField(default=0, help_text='pos\u0142ugi w tabelce obecno\u015bci s\u0105 uporz\u0105dkowane wed\u0142ugmalej\u0105cego priorytetu', verbose_name='priorytet w tabelce'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customtextconfig',
            name='obligatory',
            field=models.BooleanField(default=False, help_text='Punkty obowi\u0105zkowe pojawi\u0105 si\u0119 w ka\u017cdym sprawozdaniu.', verbose_name='obowi\u0105zkowy'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together=set([('report', 'diocese', 'service')]),
        ),
    ]
