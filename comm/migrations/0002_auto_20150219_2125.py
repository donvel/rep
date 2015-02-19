# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import comm.models


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='communionday',
            options={'verbose_name': 'Dzie\u0144 wsp\xf3lnoty', 'verbose_name_plural': 'Dni wsp\xf3lnoty'},
        ),
        migrations.AlterField(
            model_name='communionday',
            name='date',
            field=models.DateField(default=comm.models._current_date, verbose_name=b'data'),
            preserve_default=True,
        ),
    ]
