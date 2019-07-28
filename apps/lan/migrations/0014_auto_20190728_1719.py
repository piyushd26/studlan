# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-28 17:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lan', '0013_auto_20190721_0705'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendee',
            options={'ordering': ['-user', 'lan'], 'verbose_name': 'LAN attendee', 'verbose_name_plural': 'LAN attendees'},
        ),
        migrations.AlterModelOptions(
            name='directions',
            options={'verbose_name': 'LAN directions', 'verbose_name_plural': 'LAN directions'},
        ),
        migrations.AlterModelOptions(
            name='lan',
            options={'ordering': ['start_date'], 'permissions': (('export_paying_participants', 'Can export list of paying participants to downloadable file'), ('register_arrivals', 'Can register arrivals'), ('register_new_user', 'Can directly register a new user')), 'verbose_name': 'LAN', 'verbose_name_plural': 'LANs'},
        ),
        migrations.AlterModelOptions(
            name='lantranslation',
            options={'verbose_name': 'LAN translation', 'verbose_name_plural': 'LAN translations'},
        ),
        migrations.AlterModelOptions(
            name='stream',
            options={'verbose_name': 'stream', 'verbose_name_plural': 'streams'},
        ),
        migrations.AlterModelOptions(
            name='ticket',
            options={'verbose_name': 'ticket', 'verbose_name_plural': 'tickets'},
        ),
        migrations.AlterModelOptions(
            name='tickettype',
            options={'verbose_name': 'ticket type', 'verbose_name_plural': 'ticket types'},
        ),
        migrations.AlterModelOptions(
            name='tickettypetranslation',
            options={'verbose_name': 'ticket type translation', 'verbose_name_plural': 'ticket type translation'},
        ),
        migrations.AlterField(
            model_name='attendee',
            name='lan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lan.LAN', verbose_name='lan'),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='directions',
            name='description',
            field=models.TextField(blank=True, help_text='Directions.', verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='directions',
            name='lan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lan.LAN', verbose_name='lan'),
        ),
        migrations.AlterField(
            model_name='directions',
            name='title',
            field=models.TextField(verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='stream',
            name='active',
            field=models.BooleanField(default=False, help_text='No more than one stream can be active at any given time.', verbose_name='is active'),
        ),
        migrations.AlterField(
            model_name='stream',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='bought_date',
            field=models.DateField(verbose_name='bought date'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='invalid_date',
            field=models.DateField(blank=True, null=True, verbose_name='invalid date'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='invalid_description',
            field=models.TextField(blank=True, verbose_name='invalid description'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lan.TicketType', verbose_name='ticket type'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='valid',
            field=models.BooleanField(default=True, verbose_name='is valid'),
        ),
        migrations.AlterField(
            model_name='tickettype',
            name='lan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lan.LAN', verbose_name='lan'),
        ),
        migrations.AlterField(
            model_name='tickettype',
            name='number_of_seats',
            field=models.IntegerField(verbose_name='seats'),
        ),
        migrations.AlterField(
            model_name='tickettype',
            name='price',
            field=models.IntegerField(default=50, verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='tickettype',
            name='priority',
            field=models.IntegerField(default=0, help_text='In what priority the tickets will show, higher number will show first.', verbose_name='prioity'),
        ),
        migrations.AlterField(
            model_name='tickettypetranslation',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='tickettypetranslation',
            name='title',
            field=models.CharField(max_length=50, verbose_name='title'),
        ),
    ]
