# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 11:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20171020_1734'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='salepromo',
            options={'verbose_name': 'Скидка', 'verbose_name_plural': 'Скидки'},
        ),
        migrations.RemoveField(
            model_name='salepromo',
            name='condition',
        ),
        migrations.RemoveField(
            model_name='salepromo',
            name='description',
        ),
        migrations.RemoveField(
            model_name='salepromo',
            name='type',
        ),
        migrations.AlterField(
            model_name='basket',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Дата заказа'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='sum',
            field=models.IntegerField(blank=True, null=True, verbose_name='Сумма заказа, руб.'),
        ),
        migrations.AlterField(
            model_name='call',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='package',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='Цена за штуку'),
        ),
        migrations.AlterField(
            model_name='salepromo',
            name='date_start',
            field=models.DateField(default=datetime.datetime(2017, 10, 23, 11, 48, 19, 405508, tzinfo=utc), verbose_name='Дата начала скидки'),
        ),
        migrations.AlterField(
            model_name='salepromo',
            name='date_stop',
            field=models.DateField(blank=True, null=True, verbose_name='Дата окончания скидки'),
        ),
    ]