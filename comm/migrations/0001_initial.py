# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommunionDay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'kr\xc3\xb3tsza ni\xc5\xbc temat :-}', max_length=200, verbose_name=b'nazwa')),
                ('topic', models.CharField(max_length=500, verbose_name=b'temat')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'data')),
                ('handout', models.FileField(upload_to=b'konspekty', verbose_name=b'konspekt')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
