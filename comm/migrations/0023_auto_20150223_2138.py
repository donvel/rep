# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import comm.models


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0022_auto_20150223_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customtext',
            name='content',
            field=comm.models.MyHTMLField(null=True, verbose_name='tre\u015b\u0107', blank=True),
            preserve_default=True,
        ),
    ]
