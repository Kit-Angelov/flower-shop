from django.core.mail import send_mail


def send_email(type, from_to, **kwargs):
    if type == 'call':
        send_mail('Звонок',
                  'Имя: {0}\nТелефон: {1}\nДата: {2}'.format(kwargs['name'],
                                                             kwargs['phone'],
                                                             str(kwargs['order_date'])),
                  from_to[0],
                  [from_to[1]],
                  fail_silently=False,
                  )

    if type == 'order':
        elem_list = kwargs['elem_list']
        order = str()
        for attr in elem_list:
            if attr[0].startswith('Конструктор'):
                order += '--------\n{0}\nСумма: {1}\nУпаковка: {2}\n-------'.format(str(attr[0]),
                                                                                    str(attr[1]),
                                                                                    str(attr[2]))
                for attr_elem in attr[3]:
                    order += '--------\n{0}\nПродукт: {1}\nКол-во: {2}\n-------'.format(str(attr_elem[0]),
                                                                                        str(attr_elem[1]),
                                                                                        str(attr_elem[2]))
            else:
                order += '--------\nПродукт: {0}\nКол-во: {1}\nУпаковка: {2}\nСумма: {3} Р\n-------'.format(
                    str(attr[0]),
                    str(attr[1]),
                    str(attr[2]),
                    str(attr[3]))

        send_mail('Заказ',
                  'Имя: {0}\nАдрес: {1}\nТелефон: {2}\nДата заказа: {3}\nСумма заказа: {4} Р.\nДоставка: {5}\n{6}'.format(
                      kwargs['name'],
                      kwargs['address'],
                      kwargs['phone'],
                      str(kwargs['order_date']),
                      str(kwargs['order_sum']),
                      kwargs['delivery'],
                      order),
                  from_to[0],
                  [from_to[1]],
                  fail_silently=False,
                  )