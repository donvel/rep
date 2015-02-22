# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0017_auto_20150220_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conclusion',
            name='report',
        ),
        migrations.DeleteModel(
            name='Conclusion',
        ),
    ]
