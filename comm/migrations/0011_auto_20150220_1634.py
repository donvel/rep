# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0010_auto_20150220_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customtext',
            name='content',
            field=models.TextField(null=True, verbose_name='tre\u015b\u0107', blank=True),
            preserve_default=True,
        ),
    ]
