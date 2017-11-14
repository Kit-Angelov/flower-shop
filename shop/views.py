from django.shortcuts import render, get_object_or_404, render_to_response, get_list_or_404, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .models import Category, Product, Basket, BasketElem, Package, Constructor, Call
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import uuid
from hashlib import sha256
from .forms import ProductsSearchForm
from django.utils import timezone
from .telebot import send_telegram
from datetime import datetime
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .send_mail import send_email

delivery_price = 250


def index(request):
    basket = check_basket(request)
    categories = Category.objects.filter(display=True)
    products = Product.objects.filter(display=True).order_by('price')
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'shop/base.html', context=context)


def change_filters(request):
    basket = check_basket(request)
    if request.method == 'GET':
        print('REQUESTPOST', request.POST)
        category_id = request.GET.get('category')
        sort_value = request.GET.get('sort')

        if category_id == '999':
            category_set = Product.objects.filter(display=True).order_by(sort_value)
        else:
            category = Category.objects.get(id=category_id)
            category_set = category.product_set.all().order_by(sort_value)
        catalog_html = loader.render_to_string(
            'shop/catalog.html',
            {
                'products': category_set,
            }
        )
        output_data = {
            'products_set': catalog_html,
        }
        return JsonResponse(output_data)


def select_product(request):
    if request.method == 'GET':
        print('REQUESTPOST', request.POST)
        product_id = request.GET.get('product_id')
        print('product_id', product_id)
        product = Product.objects.get(id=product_id)
        if product.package is True:
            packages = Package.objects.all()
        else:
            packages = ""
        product_html = loader.render_to_string(
            'shop/infoflower_input.html',
            {
                'product_info': product,
                'packages': packages,
                'sale_price': product.sale_price
            }
        )
        print(packages)
        output_data = {
            'content': product_html,
        }

        return JsonResponse(output_data)


def add_to_basket(request):
    basket = check_basket(request)
    if request.method == 'GET':
        product_id = int(request.GET.get('product_id'))
        flower_count = int(request.GET.get('flower_count'))
        pack_id = int(request.GET.get('pack'))

        product = Product.objects.get(id=product_id)
        if pack_id == 999:
            basket_elem = BasketElem(product=product, basket=basket, count=flower_count)
        else:
            pack = Package.objects.get(id=pack_id)
            basket_elem = BasketElem(product=product, basket=basket, count=flower_count, package=pack)
        basket_elem.save()

        basket = check_basket(request)
        context = str()
        try:
            basket = Basket.objects.get(guid=request.session['guid'])
            basket_elems = basket.basketelem_set.all().filter(constructor_child=False)
            constructor_elems = basket.constructor_set.all().filter(build=True)
            context = str(len(basket_elems) + len(constructor_elems))
        except:
            context = str(0)
        finally:
            return HttpResponse(context)


def check_guid(request):
    guid = request.session.get('guid', None)
    if guid is not None:
        return guid
    else:
        guid = str(uuid.uuid4())
        request.session['guid'] = guid
        return guid


def check_basket(request):
    guid = check_guid(request)
    try:
        basket = Basket.objects.get(guid=guid)
    except Exception as e:
        print(e)
        basket = Basket(guid=guid)
        basket.save()
    return basket


def counts(request):
    try:
        basket = Basket.objects.get(uuid=request.session['uuid'])
        basket_elems = basket.basketelem_set.all()
        return {'count': str(len(basket_elems))}
    except Exception as e:
        print(e)
        return {'count': str(0)}


def basket(request):
    basket = check_basket(request)
    if request.method == 'GET':
        basket_list = basket.basketelem_set.all().filter(constructor_child=False)
        constructor_list = basket.constructor_set.all().filter(build=True)
        elem_list = list()
        for i in basket_list:
            elem_list.append(i)
        for k in constructor_list:
            elem_list.append(k)
        final_sum = final_sum_calc(basket)
        basket_set = loader.render_to_string(
            'shop/basket_input.html',
            {
                'basket_list': elem_list,
                'count_basket_elem': len(elem_list),
                'final_sum': final_sum,
                'basket_delivery': basket.delivery
            }
        )

        output_data = {
            'basket_set': basket_set,
        }
        return JsonResponse(output_data)


def delete_from_basket(request):
    if request.method == 'GET':
        elem_id = request.GET.get('elem_id')
        try:
            basket_elem = BasketElem.objects.get(id=elem_id)
        except:
            basket_elem = Constructor.objects.get(id=elem_id)

        basket_elem.delete()
        basket = check_basket(request)
        basket_list = basket.basketelem_set.all().filter(constructor_child=False)
        constructor_list = basket.constructor_set.all().filter(build=True)
        basket_count = len(basket_list) + len(constructor_list)
        elem_list = list()
        for i in basket_list:
            elem_list.append(i)
        for k in constructor_list:
            elem_list.append(k)
        final_sum = final_sum_calc(basket)
        basket_set = loader.render_to_string(
            'shop/basket_input.html',
            {
                'basket_list': elem_list,
                'count_basket_elem': basket_count,
                'final_sum': final_sum,
                'basket_delivery': basket.delivery
            }
        )

        output_data = {
            'basket_set': basket_set,
            'basket_count': basket_count,
        }
        return JsonResponse(output_data)


def change_count_in_basket(request):
    if request.method == 'GET':
        elem_id = request.GET.get('elem_id')
        attr = request.GET.get('attr')

        basket_elem = BasketElem.objects.get(id=elem_id)
        count_elem_basket_change_validator(attr, basket_elem)

        basket = check_basket(request)
        basket_list = basket.basketelem_set.all().filter(constructor_child=False)
        constructor_list = basket.constructor_set.all().filter(build=True)
        basket_count = len(basket_list) + len(constructor_list)
        elem_list = list()
        for i in basket_list:
            elem_list.append(i)
        for k in constructor_list:
            elem_list.append(k)

        final_sum = final_sum_calc(basket)
        basket_set = loader.render_to_string(
            'shop/basket_input.html',
            {
                'basket_list': elem_list,
                'count_basket_elem': basket_count,
                'final_sum': final_sum,
                'basket_delivery': basket.delivery
            }
        )
        output_data = {
            'basket_set': basket_set,
            'basket_count': basket_count,
        }
        return JsonResponse(output_data)


def count_elem_basket_change_validator(attr, basket_elem):
    count = basket_elem.count
    try:
        attr = int(attr)
        if 0 < attr < 102:
            basket_elem.count = attr
        elif attr > 101:
            basket_elem.count = 101
    except:
        if attr == 'inc' and count <= 100:
            basket_elem.count += 1
        elif attr == 'dec' and count > 1:
            basket_elem.count -= 1
    basket_elem.save()


def add_delivery(request):
    basket = check_basket(request)
    if request.method == 'GET':
        value = request.GET.get('val')
        if value == 'delivery2':
            basket.delivery = True
            basket.save()
        else:
            basket.delivery = False
            basket.save()
        final_sum = final_sum_calc(basket)
        output_data = '{0} Руб.'.format(str(final_sum))
        return HttpResponse(output_data)


def final_sum_calc(basket):
    basket_list = basket.basketelem_set.all().filter(constructor_child=False)
    constuctor_list = basket.constructor_set.all().filter(build=True)
    final_sum = sum(i.sum for i in basket_list)
    for k in constuctor_list:
        final_sum += k.sum
    if basket.delivery is True:
        return final_sum + delivery_price
    else:
        return final_sum


def search(request):
    if request.method == 'GET':
        form = ProductsSearchForm(request.GET)
        text_query = request.GET.get('q', None)
        product_list = form.search()
        packages = Package.objects.all()
        search_set = loader.render_to_string(
            'shop/search_input.html',
            {
                'search_products': product_list,
                'text_query': text_query,
                'packages': packages,
            }
        )
        output_data = {
            'search_set': search_set,
        }
        return JsonResponse(output_data)


def contact_pay(request):
    basket = check_basket(request)
    if request.method == 'GET':
        name = request.GET.get('name')
        phone = request.GET.get('phone')
        address = request.GET.get('address')

        basket.name = name
        basket.phone = phone
        basket.address = address
        basket.sum = final_sum_calc(basket)
        basket.save()

        pay_set = loader.render_to_string(
            'shop/payment_input.html',
            {
                'sum': basket.sum,
                'name': basket.name,
                'phone': basket.phone,
                'address': basket.address
            }
        )
        output_data = {
            'pay_set': pay_set,
        }
        return JsonResponse(output_data)


def popoln(request):
    basket = check_basket(request)
    mrh_login = "purpur36"
    mrh_pass1 = "hj70P4CQgxGIn1A5tiZk"
    inv_id = str(basket.id)
    inv_desc = str(basket.phone)
    out_summ = str(float(basket.sum))

    result_string = "{}:{}:{}:{}".format(mrh_login, out_summ, inv_id, mrh_pass1)
    sign_hash = sha256(result_string.encode())
    crc = sign_hash.hexdigest().upper()
    url = "https://auth.robokassa.ru/Merchant/Index.aspx?MrchLogin={}&OutSum={}&InvId={}&Desc={}&SignatureValue={}".format(
    mrh_login, out_summ, inv_id, inv_desc, crc)
    return redirect(url)


def popoln_one_click(request, one_click_id):
    one_click = Basket.objects.get(id=one_click_id)
    mrh_login = "purpur36"
    mrh_pass1 = "hj70P4CQgxGIn1A5tiZk"
    inv_id = str(one_click.id)
    inv_desc = str(one_click.phone)
    out_summ = str(float(one_click.sum))

    result_string = "{}:{}:{}:{}".format(mrh_login, out_summ, inv_id, mrh_pass1)
    sign_hash = sha256(result_string.encode())
    crc = sign_hash.hexdigest().upper()
    url = "https://auth.robokassa.ru/Merchant/Index.aspx?MrchLogin={}&OutSum={}&InvId={}&Desc={}&SignatureValue={}".format(
    mrh_login, out_summ, inv_id, inv_desc, crc)
    return redirect(url)


def select_product_one_click(request):
    if request.method == 'GET':
        product_id = request.GET.get('product_id')
        product = Product.objects.get(id=product_id)
        if product.package is True:
            packages = Package.objects.all()
        else:
            packages = ""
        product_html = loader.render_to_string(
            'shop/one_click_form_input.html',
            {
                'product_info': product,
                'packages': packages,
                'count': '1',
            }
        )
        output_data = {
            'content': product_html,
        }
        return JsonResponse(output_data)


def change_count_one_click(request):
    if request.method == 'GET':
        elem_id = request.GET.get('elem_id')
        attr = request.GET.get('attr')
        count = int(request.GET.get('count'))
        pack_id = request.GET.get('pack')
        delivery = request.GET.get('delivery')

        product = Product.objects.get(id=elem_id)

        if product.package is True:
            pack = Package.objects.get(id=pack_id)
            packages = list(Package.objects.all())
            for i in range(len(packages)):
                if packages[i] == pack:
                    package = packages.pop(i)
                    packages.insert(0, package)
            pack_price = pack.price
        else:
            packages = None
            pack_price = 0
        if delivery == 'delivery1':
            delivery_sum = 0
            delivery_check = False
        else:
            delivery_sum = delivery_price
            delivery_check = True
        try:
            attr = int(attr)
            if 0 < attr < 102:
                count = attr
            elif attr > 101:
                count = 101
        except:
            if attr == 'inc' and count <= 100:
                count += 1
            elif attr == 'dec' and count > 1:
                count -= 1
        if product.sale_price is not None:
            final_sum = product.sale_price * count + pack_price + delivery_sum
        else:
            final_sum = product.price * count + pack_price + delivery_sum
        one_click_change = loader.render_to_string(
            'shop/one_click_form_input.html',
            {
                'product_info': product,
                'packages': packages,
                'count': count,
                'final_sum': final_sum,
                'delivery_check': delivery_check
            }
        )
        output_data = {
            'one_click_info': one_click_change,
        }
        return JsonResponse(output_data)


def change_pack_one_click(request):
    if request.method == 'GET':
        elem_id = request.GET.get('elem_id')
        count = int(request.GET.get('count'))
        pack_id = request.GET.get('pack')
        delivery = request.GET.get('delivery')

        product = Product.objects.get(id=elem_id)
        if product.package is True:
            pack = Package.objects.get(id=pack_id)
            packages = list(Package.objects.all())
            for i in range(len(packages)):
                if packages[i] == pack:
                    package = packages.pop(i)
                    packages.insert(0, package)
            pack_price = pack.price
        else:
            packages = None
            pack_price = 0
        if delivery == 'delivery1':
            delivery_sum = 0
            delivery_check = False
        else:
            delivery_sum = delivery_price
            delivery_check = True

        if product.sale_price is not None:
            final_sum = product.sale_price * count + pack_price + delivery_sum
        else:
            final_sum = product.price * count + pack_price + delivery_sum
        one_click_change = loader.render_to_string(
            'shop/one_click_form_input.html',
            {
                'product_info': product,
                'packages': packages,
                'count': count,
                'final_sum': final_sum,
                'delivery_check': delivery_check
            }
        )
        output_data = {
            'one_click_info': one_click_change,
        }
        return JsonResponse(output_data)


def add_delivery_one_click(request):

    if request.method == 'GET':
        elem_id = request.GET.get('elem_id')
        count = int(request.GET.get('count'))
        pack_id = request.GET.get('pack')
        delivery = request.GET.get('delivery')

        product = Product.objects.get(id=elem_id)
        if product.package is True:
            pack = Package.objects.get(id=pack_id)
            packages = list(Package.objects.all())
            for i in range(len(packages)):
                if packages[i] == pack:
                    package = packages.pop(i)
                    packages.insert(0, package)
            pack_price = pack.price
        else:
            packages = None
            pack_price = 0
        if delivery == 'delivery1':
            delivery_sum = 0
            delivery_check = False
        else:
            delivery_sum = delivery_price
            delivery_check = True

        if product.sale_price is not None:
            final_sum = product.sale_price * count + pack_price + delivery_sum
        else:
            final_sum = product.price * count + pack_price + delivery_sum
        one_click_change = loader.render_to_string(
            'shop/one_click_form_input.html',
            {
                'product_info': product,
                'packages': packages,
                'count': count,
                'final_sum': final_sum,
                'delivery_check': delivery_check
            }
        )
        output_data = {
            'one_click_info': one_click_change,
        }
        return JsonResponse(output_data)


def make_order_one_click(request):
    if request.method == 'GET':
        guid = uuid.uuid4()
        name = request.GET.get('name')
        phone = request.GET.get('phone')
        address = request.GET.get('address')
        count = int(request.GET.get('count'))
        pack_id = request.GET.get('pack')
        delivery = request.GET.get('delivery')
        elem_id = request.GET.get('elem_id')

        product = Product.objects.get(id=elem_id)
        if product.package is True:
            pack = Package.objects.get(id=pack_id)
            packages = list(Package.objects.all())
            for i in range(len(packages)):
                if packages[i] == pack:
                    package = packages.pop(i)
                    packages.insert(0, package)
            pack_price = pack.price
        else:
            pack = None
            pack_price = 0

        if delivery == 'delivery1':
            delivery_check = False
            delivery_sum = 0
        else:
            delivery_check = True
            delivery_sum = delivery_price

        if product.sale_price is not None:
            sum = product.sale_price * count + pack_price + delivery_sum
        else:
            sum = product.price * count + pack_price + delivery_sum
        one_click_basket = Basket(
            guid=guid,
            sum=sum,
            name=name,
            phone=phone,
            address=address,
            delivery=delivery_check,
        )
        one_click_basket.save()

        one_click_basket_elem = BasketElem(
            product=product,
            basket=one_click_basket,
            count=count,
            package=pack,
        )
        one_click_basket_elem.save()

        pay_set = loader.render_to_string(
            'shop/payment_input.html',
            {
                'one_click': 'ok',
                'one_click_id': one_click_basket.id,
                'sum': one_click_basket.sum,
                'name': one_click_basket.name,
                'phone': one_click_basket.phone,
                'address': one_click_basket.address
            }
        )
        output_data = {
            'pay_set': pay_set,
        }
        return JsonResponse(output_data)


def change_filters_in_constructor(request):
    basket = check_basket(request)
    if request.method == 'GET':
        category_id = request.GET.get('category')

        if category_id == '999':
            category_set = Product.objects.filter(display=True).order_by('price')
        else:
            category = Category.objects.get(id=category_id)
            category_set = category.product_set.all().filter(display=True).order_by('price')
        catalog_html = loader.render_to_string(
            'shop/catalog_in_constructor.html',
            {
                'products': category_set,
            }
        )
        output_data = {
            'products_set': catalog_html,
        }
        return JsonResponse(output_data)


def add_to_basket_in_constructor(request):
    basket = check_basket(request)
    if request.method == 'GET':
        product_id = request.GET.get('product_id')
        count = request.GET.get('count')
        pack_id = request.GET.get('pack_id')
        try:
            constructor = Constructor.objects.get(basket=basket, build=False)
        except:
            constructor = Constructor(basket=basket)
            constructor.save()
        product = Product.objects.get(id=product_id)
        basket_elem = BasketElem(product=product,
                                 basket=basket,
                                 count=count,
                                 constructor_child=True,
                                 constructor=constructor)
        basket_elem.save()
        basket_elem_list = BasketElem.objects.all().filter(basket=basket, constructor=constructor)
        constructor_products = loader.render_to_string(
            'shop/basket_in_constructor.html',
            {
                'basket_constructor_elems': basket_elem_list,
            }
        )
        pack = Package.objects.get(id=pack_id)
        final_sum = pack.price
        for elem in basket_elem_list:
            final_sum += elem.sum
        output_data = {
            'constructor_products': constructor_products,
            'final_sum_constructor': '{} Руб'.format(final_sum)
        }

        return JsonResponse(output_data)


def openconstructor(request):
    basket = check_basket(request)
    if request.method == 'GET':
        try:
            constructor = Constructor.objects.get(basket=basket, build=False)
        except:
            constructor = Constructor(basket=basket)
            constructor.save()

        basket_elem_list = BasketElem.objects.all().filter(basket=basket, constructor=constructor)
        constructor_products = loader.render_to_string(
            'shop/basket_in_constructor.html',
            {
                'basket_constructor_elems': basket_elem_list,
            }
        )

        category_set = Product.objects.filter(display=True).order_by('price')
        catalog_html = loader.render_to_string(
            'shop/catalog_in_constructor.html',
            {
                'products': category_set,
            }
        )
        pack = Package.objects.all()
        final_sum = pack[0].price
        for elem in basket_elem_list:
            final_sum += elem.sum

        packages_html = loader.render_to_string(
            'shop/pack_costructor.html',
            {
                'packages_constructor': pack,
            }
        )

        output_data = {
            'constructor_products': constructor_products,
            'final_sum_constructor': '{} Руб'.format(final_sum),
            'catalog_html': catalog_html,
            'packages_constructor': packages_html
        }

        return JsonResponse(output_data)


def change_pack_in_constructor(request):
    basket = check_basket(request)
    if request.method == 'GET':
        pack_id = request.GET.get('pack')
        pack = Package.objects.get(id=pack_id)

        try:
            constructor = Constructor.objects.get(basket=basket, build=False)
        except:
            constructor = Constructor(basket=basket)
            constructor.save()

        basket_elem_list = BasketElem.objects.all().filter(basket=basket, constructor=constructor)
        final_sum = pack.price
        for elem in basket_elem_list:
            final_sum += elem.sum
        output_data = {
            'final_sum_constructor': '{} Руб'.format(final_sum)
        }

        return JsonResponse(output_data)


def delete_from_lego_flower(request):
    basket = check_basket(request)
    if request.method == 'GET':
        elem_id = request.GET.get('elem_id')
        pack_id = request.GET.get('pack_id')
        try:
            constructor = Constructor.objects.get(basket=basket, build=False)
        except:
            constructor = Constructor(basket=basket)
            constructor.save()
        basket_elem = BasketElem.objects.get(id=elem_id)
        basket_elem.delete()
        basket_elem_list = BasketElem.objects.all().filter(basket=basket, constructor=constructor)
        constructor_products = loader.render_to_string(
            'shop/basket_in_constructor.html',
            {
                'basket_constructor_elems': basket_elem_list,
            }
        )
        pack = Package.objects.get(id=pack_id)
        final_sum = pack.price
        for elem in basket_elem_list:
            final_sum += elem.sum
        output_data = {
            'constructor_products': constructor_products,
            'final_sum_constructor': '{} Руб'.format(final_sum)
        }

        return JsonResponse(output_data)


def add_to_basket_constructor(request):
    basket = check_basket(request)
    if request.method == 'GET':
        pack_id = request.GET.get('pack_id')
        pack = Package.objects.get(id=pack_id)
        try:
            constructor = Constructor.objects.get(basket=basket, build=False)
        except:
            constructor = Constructor(basket=basket)
            constructor.save()
        basket_elem_list = BasketElem.objects.all().filter(basket=basket, constructor=constructor)
        final_sum = pack.price
        for elem in basket_elem_list:
            final_sum += elem.sum
        constructor.sum = final_sum
        constructor.build = True
        constructor.package = pack
        constructor.save()
        basket_elems = BasketElem.objects.all().filter(basket=basket, constructor_child=False)
        constructors = Constructor.objects.all().filter(basket=basket, build=True)
        basket_list = list()
        for i in basket_elems:
            basket_list.append(i)
        for k in constructors:
            basket_list.append(k)
        count_basket = len(basket_list)
        context = str(count_basket)
        return HttpResponse(context)


def call(request):
    if request.method == 'GET':
        phone = request.GET.get('phone')
        name = request.GET.get('name')
        call = Call(name=name, phone=phone)
        call.save()
        send_email(type="call", from_to=['kit.angelov@gmail.com', 'dimkabelyaev@gmail.com'],
                   name=name,
                   phone=phone,
                   order_date=datetime.now().strftime("%Y.%m.%d %H:%M"))
        send_telegram(type='call',
                      name=name,
                      phone=phone,
                      order_date=datetime.now().strftime("%Y.%m.%d %H:%M"))
        return HttpResponse()


@csrf_exempt
def res(request):
    if not request.method == 'GET':
        return HttpResponse('error')
    mrh_pass2 = "m5d0r3C7NVH2wmXFPgqx"
    if request.method == 'GET':
        request.session['guid'] = None
        out_summ = request.GET['OutSum']
        inv_id = request.GET['InvId']
        crc = request.GET['SignatureValue']
        crc = crc.upper()
        crc = str(crc)
        result_string = "{}:{}:{}".format(out_summ, inv_id, mrh_pass2)
        sign_hash = sha256(result_string.encode())
        my_crc = sign_hash.hexdigest().upper()
        if my_crc not in crc:
            context = "bad sign"
            return HttpResponse(context)
        else:
            basket = Basket.objects.get(id=inv_id)
            basket.complite = True
            basket.save()
            basket_elems = basket.basketelem_set.all()
            basket_constructors = basket.constructor_set.all()
            elem_list = list()
            for elem in basket_elems:
                if elem.constructor_child is False:
                    attr = [str(elem.product.name),
                            str(elem.count),
                            str(elem.package.name),
                            str(elem.sum)]
                    elem_list.append(attr)

            for constructor_elem in basket_constructors:
                if constructor_elem.build is True:
                    constructor_elem_elems = constructor_elem.basketelem_set
                    attr = [
                        str('Конструктор {0}'.format(constructor_elem.id)),
                        str(constructor_elem.sum),
                        str(constructor_elem.package.name)
                    ]
                    attr_elems = list()
                    for i in constructor_elem_elems:
                        attr_elem = [
                            str('Элемент конструктора {0}'.format(i.constructor_child.id)),
                            str(i.product.name),
                            str(i.count),
                        ]
                        attr_elems.append(attr_elem)
                    attr.append(attr_elems)
                    elem_list.append(attr)

            categories = Category.objects.filter(display=True)
            products = Product.objects.filter(display=True).order_by('price')
            context = {
                'categories': categories,
                'products': products,
                'success_popup': True,
            }
            send_email(type="order", from_to=['kit.angeov@gmail.com', 'dimkabelyaev@gmail.co,'],
                       name=basket.name,
                       address=basket.address,
                       phone=basket.phone,
                       order_date=basket.date_upload.strftime("%Y.%m.%d %H:%M"),
                       order_sum=basket.sum,
                       elem_list=elem_list)
            send_telegram(type='order',
                          name=basket.name,
                          address=basket.address,
                          phone=basket.phone,
                          order_date=basket.date_upload.strftime("%Y.%m.%d %H:%M"),
                          order_sum=basket.sum,
                          elem_list=elem_list)
            return render(request, 'shop/base.html', context=context)


@csrf_exempt
def success(request):
    if not request.method == 'GET':
        return HttpResponse('error')
    mrh_pass1 = "hj70P4CQgxGIn1A5tiZk"
    if request.method == 'GET':
        request.session['guid'] = None
        out_summ = request.GET['OutSum']
        inv_id = request.GET['InvId']
        crc = request.GET['SignatureValue']
        crc = crc.upper()
        crc = str(crc)
        result_string = "{}:{}:{}".format(out_summ, inv_id, mrh_pass1)
        sign_hash = sha256(result_string.encode())
        my_crc = sign_hash.hexdigest().upper()
        if my_crc not in crc:
            context = "bad sign"
            return HttpResponse(context)
        else:
            categories = Category.objects.filter(display=True)
            products = Product.objects.filter(display=True).order_by('price')
            context = {
                'categories': categories,
                'products': products,
                'success_popup': True,
            }
            return render(request, 'shop/base.html', context=context)


@csrf_exempt
def fail(request):
    if request.method == "GET":
        categories = Category.objects.filter(display=True)
        products = Product.objects.filter(display=True).order_by('price')
        context = {
            'categories': categories,
            'products': products,
            'fail_popup': True,
        }
        return render(request, 'shop/base.html', context=context)

