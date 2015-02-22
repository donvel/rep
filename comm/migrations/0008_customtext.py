# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comm', '0007_auto_20150220_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomText',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(verbose_name='tre\u015b\u0107')),
                ('config', models.ForeignKey(verbose_name='w\u0142asne pole', to='comm.CustomTextConfig')),
                ('report', models.ForeignKey(verbose_name='sprawozdanie', to='comm.Report')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
