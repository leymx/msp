# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='money',
            name='person',
            field=models.CharField(max_length=128, null=True, verbose_name='\u6301\u6709\u4eba', blank=True),
        ),
    ]
