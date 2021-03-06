# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 13:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20171025_1440'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Settings',
        ),
        migrations.AddField(
            model_name='basket',
            name='delivery_sum',
            field=models.IntegerField(default=250, verbose_name='Цена доставки'),
        ),
        migrations.AlterField(
            model_name='salepromo',
            name='date_start',
            field=models.DateField(default=datetime.datetime(2017, 10, 25, 13, 40, 15, 21022, tzinfo=utc), verbose_name='Дата начала скидки'),
        ),
    ]
