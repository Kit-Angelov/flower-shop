# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 00:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20171014_1531'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basket',
            old_name='uuid',
            new_name='guid',
        ),
        migrations.AlterField(
            model_name='basket',
            name='date',
            field=models.DateField(default=datetime.date(2017, 10, 15), verbose_name='Дата заказа'),
        ),
        migrations.AlterField(
            model_name='call',
            name='date',
            field=models.DateField(default=datetime.date(2017, 10, 15), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='salepromo',
            name='date_start',
            field=models.DateField(default=datetime.date(2017, 10, 15), verbose_name='Дата начала акции/скидки'),
        ),
    ]
