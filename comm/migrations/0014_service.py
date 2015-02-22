# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0013_auto_20150220_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=100, verbose_name='pe\u0142na nazwa')),
                ('short_name', models.CharField(help_text=b'max 10 znak\xc3\xb3w, np. MDDK', max_length=10, verbose_name='kr\xf3tka nazwa')),
            ],
            options={
                'verbose_name': 'pos\u0142uga',
                'verbose_name_plural': 'pos\u0142ugi',
            },
            bases=(models.Model,),
        ),
    ]
