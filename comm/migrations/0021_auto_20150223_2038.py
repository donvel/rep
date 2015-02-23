# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0020_auto_20150223_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='display_prioirity',
            field=models.IntegerField(default=0, help_text='pos\u0142ugi w tabelce obecno\u015bci s\u0105 uporz\u0105dkowane wed\u0142ug malej\u0105cego priorytetu', verbose_name='priorytet w tabelce'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='service',
            name='short_name',
            field=models.CharField(help_text=b'max 10 znak\xc3\xb3w, np. MDDK', unique=True, max_length=10, verbose_name='kr\xf3tka nazwa'),
            preserve_default=True,
        ),
    ]
