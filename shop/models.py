from django.db import models
from django.utils import timezone


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
    name = models.CharField(max_length=30, verbose_name='Название')
    percent = models.IntegerField(verbose_name='Процент скидки', null=True, blank=True)
    date_start = models.DateField(verbose_name='Дата начала скидки', default=timezone.now())
    date_stop = models.DateField(verbose_name='Дата окончания скидки', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    parent = models.ForeignKey('self', verbose_name='Родительская категория', null=True, blank=True)
    priority = models.IntegerField(verbose_name='Приоритет',
                                   null=True,
                                   blank=True,
                                   help_text='Чем больше число, тем выше приоритет')
    display = models.BooleanField(default=False, verbose_name='Показывать')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Package(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    photo = models.ImageField(upload_to='photo_package', verbose_name='Фото', null=True, blank=True)
    description = models.TextField(max_length=300, verbose_name='Описание упаковки', null=True, blank=True)
    price = models.IntegerField(verbose_name='Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Упаковка'
        verbose_name_plural = 'Упаковки'


class Call(models.Model):
    date = models.DateField(auto_now=True, verbose_name='Дата')
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Имя')
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name='Телефон')
    closed = models.BooleanField(default=False, verbose_name='Звонок выполнен')

    def __str__(self):
        return '{0}, {1}'.format(self.date, self.name)

    class Meta:
        verbose_name = 'Заказ звонка'
        verbose_name_plural = 'Заказы звонка'


class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена за штуку')
    sale_price = models.IntegerField(verbose_name='Цена с акцией', editable=False, default=None)
    description = models.TextField(max_length=300, verbose_name='Описание')
    photo = models.ImageField(upload_to='photo_product', verbose_name='Фото')
    display = models.BooleanField(default=False, verbose_name='Отображать на сайте?')
    attribute = models.ForeignKey(Attribute, verbose_name='Характеристики', null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name='Категория', null=True, blank=True)
    sale_promo = models.ForeignKey(SalePromo, verbose_name='Акция/Скидка', null=True, blank=True, default=None)
    package = models.BooleanField(default=False, verbose_name='Есть выбор упаковки?')

    def __str__(self):
        return self.name

    @property
    def sale_price(self):
        if self.sale_promo is not None and self.sale_promo.date_start <= timezone.now().date() <= self.sale_promo.date_stop:
            return int(self.price * ((100 - self.sale_promo.percent) / 100))
        else:
            return None

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Basket(models.Model):
    guid = models.CharField(max_length=36, verbose_name='Идентификатор заказчика')
    sum = models.IntegerField(blank=True, null=True, verbose_name='Сумма заказа, руб.')
    date = models.DateField(auto_now=True, verbose_name='Дата заказа')
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Имя заказчика')
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name='Телефон заказчика')
    complite = models.BooleanField(default=False, verbose_name='Заказ оформлен')
    closed = models.BooleanField(default=False, verbose_name='Заказ завершен')

    # # доставка товаров корзины
    # delivery = models.BooleanField(default=False, verbose_name='Доставка')
    # delivery_sum = models.FloatField(blank=False, default=250, verbose_name='Сумма доставки, руб.')

    def __str__(self):
        return '{0}, {1}, {2}, {3}'.format(self.date, self.sum, self.complite, self.closed)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class BasketElem(models.Model):
    product = models.ForeignKey(Product, verbose_name='Товар')
    basket = models.ForeignKey(Basket, verbose_name='Заказ')
    count = models.IntegerField(verbose_name='Кол-во штук товара')
    sum = models.IntegerField(default=0, verbose_name='Сумма заказа, руб.')
    package = models.ForeignKey(Package, null=True)

    @property
    def sum(self):
        if self.product.sale_price is not None:
            if self.package is not None:
                return (self.count * self.product.sale_price) + self.package.price
            else:
                return self.count * self.product.sale_price
        else:
            if self.package is not None:
                return (self.count * self.product.price) + self.package.price
            else:
                return self.count * self.product.price

    def add_total_sum(self):
        self.basket.sum += self.basket.sum + self.sum

    def __str__(self):
        return '{0}, {1}'.format(self.product, self.sum)

    class Meta:
        verbose_name = 'Элемент корзины'
        verbose_name_plural = 'Элементы корзины'
