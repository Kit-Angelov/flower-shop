# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 18:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_auto_20171102_0148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oneclick',
            name='package',
        ),
        migrations.RemoveField(
            model_name='oneclick',
            name='product',
        ),
        migrations.AlterField(
            model_name='basket',
            name='complite',
            field=models.BooleanField(default=False, verbose_name='Заказ оплачен'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 10, 18, 11, 43, 716808, tzinfo=utc), verbose_name='Дата заказа'),
        ),
        migrations.AlterField(
            model_name='basketelem',
            name='package',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Package'),
        ),
        migrations.AlterField(
            model_name='call',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 10, 18, 11, 43, 714573, tzinfo=utc), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='salepromo',
            name='date_start',
            field=models.DateField(default=datetime.datetime(2017, 11, 10, 18, 11, 43, 712700, tzinfo=utc), verbose_name='Дата начала скидки'),
        ),
        migrations.DeleteModel(
            name='OneClick',
        ),
    ]
