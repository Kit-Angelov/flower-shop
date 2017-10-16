# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 10:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('county', models.CharField(blank=True, max_length=20, null=True, verbose_name='Страна')),
                ('length', models.IntegerField(blank=True, null=True, verbose_name='Длина стебля')),
            ],
            options={
                'verbose_name': 'Аттрибуты товара',
                'verbose_name_plural': 'Аттрибуты товара',
            },
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=36, verbose_name='Идентификатор заказчика')),
                ('sum', models.FloatField(blank=True, null=True, verbose_name='Сумма заказа, руб.')),
                ('date', models.DateField(default=datetime.date(2017, 10, 4), verbose_name='Дата заказа')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Имя заказчика')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Телефон заказчика')),
                ('complite', models.BooleanField(default=False, verbose_name='Заказ оформлен')),
                ('closed', models.BooleanField(default=False, verbose_name='Заказ завершен')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
            },
        ),
        migrations.CreateModel(
            name='BasketElem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Кол-во штук товара')),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Basket', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Элемент корзины',
                'verbose_name_plural': 'Элементы корзины',
            },
        ),
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date(2017, 10, 4), verbose_name='Дата')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Имя')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Телефон')),
                ('closed', models.BooleanField(default=False, verbose_name='Звонок выполнен')),
            ],
            options={
                'verbose_name': 'Заказ звонка',
                'verbose_name_plural': 'Заказы звонка',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('priority', models.IntegerField(blank=True, help_text='Чем больше число, тем выше приоритет', null=True, verbose_name='Приоритет')),
                ('display', models.BooleanField(default=False, verbose_name='Отображать на сайте?')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Category', verbose_name='Родительская категория')),
            ],
            options={
                'verbose_name': 'Категрия',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Decorator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo_decor', verbose_name='Фото')),
                ('description', models.TextField(blank=True, max_length=300, null=True, verbose_name='Описание декораторов')),
                ('price', models.FloatField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Декоратор',
                'verbose_name_plural': 'Декораторы',
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo_package', verbose_name='Фото')),
                ('description', models.TextField(blank=True, max_length=300, null=True, verbose_name='Описание упаковки')),
                ('price', models.FloatField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Упаковка',
                'verbose_name_plural': 'Упаковки',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('price', models.FloatField(verbose_name='Цена за штуку')),
                ('description', models.TextField(max_length=300, verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='photo_product', verbose_name='Фото')),
                ('display', models.BooleanField(default=False, verbose_name='Отображать на сайте?')),
                ('package', models.BooleanField(default=False, verbose_name='Есть выбор упаковки?')),
                ('decor', models.BooleanField(default=False, verbose_name='Есть выбор декорирования?')),
                ('attribute', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Attribute', verbose_name='Характеристики')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='SalePromo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('sale', 'Скидка'), ('prom', 'Акция')], default='sale', max_length=4)),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('percent', models.IntegerField(blank=True, null=True, verbose_name='Процент скидки')),
                ('description', models.TextField(blank=True, max_length=300, null=True, verbose_name='Описание акции')),
                ('condition', models.IntegerField(blank=True, help_text='кол-во цветов необходимое для работы акции', null=True, verbose_name='Условия акции')),
                ('date_start', models.DateField(default=datetime.date(2017, 10, 4), verbose_name='Дата начала акции/скидки')),
                ('date_stop', models.DateField(blank=True, null=True, verbose_name='Дата окончания акции/скидки')),
            ],
            options={
                'verbose_name': 'Скидка/Акции',
                'verbose_name_plural': 'Аттрибуты товара',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='sale_promo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.SalePromo', verbose_name='Акция/Скидка'),
        ),
        migrations.AddField(
            model_name='basketelem',
            name='decor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Decorator', verbose_name='Декоратор'),
        ),
        migrations.AddField(
            model_name='basketelem',
            name='pack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Package', verbose_name='Упаковка'),
        ),
        migrations.AddField(
            model_name='basketelem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product', verbose_name='Товар'),
        ),
    ]