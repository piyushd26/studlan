# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0012_auto_20160212_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registertoken',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 9, 14, 47, 7, 695587), verbose_name=b'created', auto_now_add=True),
            preserve_default=True,
        ),
    ]
