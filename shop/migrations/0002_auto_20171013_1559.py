# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-13 12:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElemSort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sorted', models.CharField(max_length=20, verbose_name='Указатель сортировки')),
            ],
            options={
                'verbose_name': 'Элемент сортировка',
            },
        ),
        migrations.CreateModel(
            name='Sort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Сортировка',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categorys'},
        ),
        migrations.AlterField(
            model_name='basket',
            name='date',
            field=models.DateField(default=datetime.date(2017, 10, 13), verbose_name='Дата заказа'),
        ),
        migrations.AlterField(
            model_name='call',
            name='date',
            field=models.DateField(default=datetime.date(2017, 10, 13), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='category',
            name='display',
            field=models.BooleanField(default=False, verbose_name='Показывать'),
        ),
        migrations.AlterField(
            model_name='salepromo',
            name='date_start',
            field=models.DateField(default=datetime.date(2017, 10, 13), verbose_name='Дата начала акции/скидки'),
        ),
        migrations.AddField(
            model_name='elemsort',
            name='sort',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Sort', verbose_name='Добавить в сортировку'),
        ),
        migrations.AddField(
            model_name='category',
            name='sort',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Sort', verbose_name='Сортировка'),
        ),
    ]