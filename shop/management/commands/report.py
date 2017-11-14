from django.core.management.base import BaseCommand, CommandError
from shop.models import Product, Basket, BasketElem, Package
from django.utils import timezone
import csv
from datetime import date


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('last_date_report.txt', 'r') as file:
            last_date = file.read()
            last_date = timezone.datetime.strptime(last_date, "%Y-%m-%d %H:%M:%S.%f")
        new_date = timezone.now()
        with open('last_date_report.txt', 'w') as file:
            file.write(str(new_date)[:-6])
        list_basket = Basket.objects.filter(date__range=[last_date, new_date], complite=True)
        list_reports = list()
        for elem in list_basket:
            basket_elems = elem.basketelem_set.all()
            for i in basket_elems:
                name = i.product.name
                count = str(i.count)
                try:
                    package = i.package.name
                except:
                    package = ''
                list_reports.append([name, count, package])
        with open('report {0}.csv'.format(date.today()), "w", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            writer.writerow(['Наименование',
                             'Количество',
                             'Упаковка',
                             'Дата начала {0}'.format(last_date),
                             'Дата окончания {0}'.format(str(new_date)[:-6])])
            for i in list_reports:
                writer.writerow(i)
