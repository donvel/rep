# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0011_auto_20150220_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='file_report',
            field=models.FileField(help_text='tradycyjne sprawozdanie (np. .doc lub .pdf)', upload_to=b'sprawozdania', null=True, verbose_name=b'dokument sprawozdania', blank=True),
            preserve_default=True,
        ),
    ]
