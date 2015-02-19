# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0002_auto_20150219_2125'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='communionday',
            options={'verbose_name': 'Dzie\u0144 Wsp\xf3lnoty', 'verbose_name_plural': 'Dni Wsp\xf3lnoty'},
        ),
        migrations.AlterField(
            model_name='communionday',
            name='handout',
            field=models.FileField(upload_to=b'konspekty', null=True, verbose_name=b'konspekt', blank=True),
            preserve_default=True,
        ),
    ]
