# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0018_auto_20150221_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='customtextconfig',
            name='use_in_report',
            field=models.BooleanField(default=False, help_text='Czy uwzgl\u0119dni\u0107 w zbiorczym raporcie z DWDD.', verbose_name='w raporcie zbiorczym'),
            preserve_default=True,
        ),
    ]
