# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='money',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField(null=True, verbose_name='\u91d1\u989d', blank=True)),
                ('bank', models.CharField(max_length=128, null=True, verbose_name='\u94f6\u884c', blank=True)),
                ('buy_date', models.DateField(null=True, verbose_name='\u8d2d\u4e70\u65e5\u671f', blank=True)),
                ('valid_date', models.DateField(null=True, verbose_name='\u751f\u6548\u65e5\u671f', blank=True)),
                ('financial_type', models.CharField(max_length=255, null=True, verbose_name='\u7406\u8d22\u7c7b\u578b', blank=True)),
                ('finish_date', models.DateField(null=True, verbose_name='\u7ed3\u675f\u65e5\u671f', blank=True)),
                ('return_rate', models.FloatField(null=True, verbose_name='\u6536\u76ca\u7387', blank=True)),
                ('latest_value', models.FloatField(null=True, verbose_name='\u5f53\u524d\u51c0\u503c', blank=True)),
                ('latest_date', models.DateField(null=True, verbose_name='\u66f4\u65b0\u65e5\u671f', blank=True)),
            ],
            options={
                'db_table': 'money_info',
            },
        ),
    ]
