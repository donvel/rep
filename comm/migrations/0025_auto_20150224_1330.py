# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0024_auto_20150224_1324'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customtextconfig',
            options={'verbose_name': 'typ pola', 'verbose_name_plural': 'typy p\xf3l'},
        ),
        migrations.AddField(
            model_name='customtextconfig',
            name='display_priority',
            field=models.IntegerField(default=0, help_text='pola w sprawozdaniu s\u0105 uporz\u0105dkowane wed\u0142ug malej\u0105cego priorytetu', verbose_name='priorytet w sprawozdaniu'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='customtext',
            unique_together=set([]),
        ),
    ]
