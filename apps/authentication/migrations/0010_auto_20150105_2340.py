# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_auto_20150103_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registertoken',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 5, 23, 40, 15, 145943), verbose_name=b'created', auto_now_add=True),
            preserve_default=True,
        ),
    ]
