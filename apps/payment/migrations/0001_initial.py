# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-04 09:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lan', '0015_auto_20190730_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='LANTicketPurchaseLock',
            fields=[
                ('lan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='ticket_purchase_lock', serialize=False, to='lan.LAN', verbose_name='lan')),
            ],
            options={
                'verbose_name': 'LAN ticket purchase lock',
                'verbose_name_plural': 'LAN ticket purchase locks',
            },
        ),
    ]
