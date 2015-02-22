# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0012_report_file_report'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conclusion',
            options={'verbose_name': 'wniosek', 'verbose_name_plural': 'g\u0142\xf3wne wnioski'},
        ),
        migrations.AlterField(
            model_name='customtext',
            name='content',
            field=tinymce.models.HTMLField(null=True, verbose_name='tre\u015b\u0107', blank=True),
            preserve_default=True,
        ),
    ]
