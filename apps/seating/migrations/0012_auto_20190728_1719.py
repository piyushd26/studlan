# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-28 17:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seating', '0011_auto_20190401_2142'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='layout',
            options={'verbose_name': 'seating layout', 'verbose_name_plural': 'seating layouts'},
        ),
        migrations.AlterModelOptions(
            name='seat',
            options={'verbose_name': 'seat', 'verbose_name_plural': 'seats'},
        ),
        migrations.AlterModelOptions(
            name='seating',
            options={'permissions': (('export_seating', 'Can export seating to downloadable file'),), 'verbose_name': 'seating', 'verbose_name_plural': 'seatings'},
        ),
        migrations.AlterField(
            model_name='layout',
            name='template',
            field=models.TextField(blank=True, verbose_name='SVG layout for seating'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='placement',
            field=models.IntegerField(help_text='A unique ID within the seating.', verbose_name='placement ID'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seating',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seating.Seating', verbose_name='seating'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='seating',
            name='lan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lan.LAN', verbose_name='lan'),
        ),
        migrations.AlterField(
            model_name='seating',
            name='layout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seating.Layout', verbose_name='layout'),
        ),
        migrations.AlterField(
            model_name='seating',
            name='number_of_seats',
            field=models.IntegerField(default=0, help_text='This field is automatically updated to match the chosen layout. Change the chosen layout to alter this field.', verbose_name='number of seats'),
        ),
        migrations.AlterField(
            model_name='seating',
            name='ticket_types',
            field=models.ManyToManyField(blank=True, related_name='ticket_types', to='lan.TicketType', verbose_name='ticket types'),
        ),
    ]
