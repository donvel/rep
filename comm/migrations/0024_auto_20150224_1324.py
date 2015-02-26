# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0023_auto_20150223_2138'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='customtext',
            unique_together=set([('report', 'config')]),
        ),
    ]
