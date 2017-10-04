from django.db import models
from datetime import date


class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    price = models.FloatField(verbose_name='Цена за штуку')
    description = models.TextField(max_length=300, verbose_name='Описание')
    photo = models.ImageField(upload_to='photo_product', verbose_name='Фото')
    display = models.BooleanField(default=False, verbose_name='Отображать на сайте?')
    attr = models.ForeignKey(Attribute, verbose_name='Характеристики', null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name='Категория', null=True, blank=True)
    sale_promo = models.ForeignKey(SalePromo, verbose_name='Акция/Скидка', null=True, blank=True)
    package = models.BooleanField(default=False, verbose_name='Есть выбор упаковки?')
    decor = models.BooleanField(default=False, verbose_name='Есть выбор декорирования?')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Attribute(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    county = models.CharField(max_length=20, verbose_name='Страна', null=True, blank=True)
    length = models.IntegerField(verbose_name='Длина стебля', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Аттрибуты товара'
        verbose_name_plural = 'Аттрибуты товара'


class SalePromo(models.Model):
    types = (
        ('sale', 'Скидка'),
        ('prom', 'Акция')
    )
    type = models.CharField(max_length=4, choices=types, default='sale')
    name = models.CharField(max_length=30, verbose_name='Название')
    percent = models.IntegerField(verbose_name='Процент скидки', null=True, blank=True)
    description = models.TextField(max_length=300, verbose_name='Описание акции', null=True, blank=True)
    condition = models.IntegerField(verbose_name='Условия акции',
                                    null=True,
                                    blank=True,
                                    help_text='кол-во цветов необходимое для работы акции')
    date_start = models.DateField(verbose_name='Дата начала акции/скидки', default=date.today())
    date_stop = models.DateField(verbose_name='Дата окончания акции/скидки', null=True, blank=True)

    def __str__(self):
        return '{0}, {1}'.format(self.type, self.name)

    class Meta:
        verbose_name = 'Скидка/Акции'
        verbose_name_plural = 'Аттрибуты товара'


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    parent = models.ForeignKey('self', verbose_name='Родительская категория', null=True, blank=True)
    priority = models.IntegerField(verbose_name='Приоритет',
                                   null=True,
                                   blank=True,
                                   help_text='Чем больше число, тем выше приоритет')
    display = models.BooleanField(default=False, verbose_name='Отображать на сайте?')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категрия'
        verbose_name_plural = 'Категории'


class Package(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    photo = models.ImageField(upload_to='photo_package', verbose_name='Фото', null=True, blank=True)
    description = models.TextField(max_length=300, verbose_name='Описание упаковки', null=True, blank=True)
    price = models.FloatField(verbose_name='Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Упаковка'
        verbose_name_plural = 'Упаковки'


class Decorator(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    photo = models.ImageField(upload_to='photo_decor', verbose_name='Фото', null=True, blank=True)
    description = models.TextField(max_length=300, verbose_name='Описание декораторов', null=True, blank=True)
    price = models.FloatField(verbose_name='Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Декоратор'
        verbose_name_plural = 'Декораторы'


class Basket(models.Model):
    uuid = models.CharField(max_length=36, verbose_name='Идентификатор заказчика')
    sum = models.FloatField(blank=True, null=True, verbose_name='Сумма заказа, руб.')
    date = models.DateField(default=date.today(), verbose_name='Дата заказа')
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Имя заказчика')
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name='Телефон заказчика')
    complite = models.BooleanField(default=False, verbose_name='Заказ оформлен')
    closed = models.BooleanField(default=False, verbose_name='Заказ завершен')

    def __str__(self):
        return '{0}, {1}, {2}, {3}'.format(self.date, self.sum, self.complite, self.closed)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class BasketElem(models.Model):
    product = models.ForeignKey(Product, verbose_name='Товар')
    basket = models.ForeignKey(Basket, verbose_name='Заказ')
    count = models.IntegerField(verbose_name='Кол-во штук товара')
    pack = models.ForeignKey(Package, verbose_name='Упаковка')
    decor = models.ForeignKey(Decorator, verbose_name='Декоратор')
    sum = models.FloatField(default=0, verbose_name='Сумма заказа, руб.')

    @property
    def sum(self):
        return self.count * self.product.price

    def add_total_sum(self):
        self.basket.sum += self.basket.sum + self.sum

    def __str__(self):
        return '{0}, {1}'.format(self.product, self.sum)

    class Meta:
        verbose_name = 'Элемент корзины'
        verbose_name_plural = 'Элементы корзины'


class Call(models.Model):
    date = models.DateField(default=date.today(), verbose_name='Дата')
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Имя')
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name='Телефон')
    closed = models.BooleanField(default=False, verbose_name='Звонок выполнен')

    def __str__(self):
        return '{0}, {1}'.format(self.date, self.name)

    class Meta:
        verbose_name = 'Заказ звонка'
        verbose_name_plural = 'Заказы звонка'
