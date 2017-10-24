from django.shortcuts import render, get_object_or_404, render_to_response, get_list_or_404
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .models import Category, Product, Basket, BasketElem, Package
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import uuid
from .forms import ProductsSearchForm
from django.utils import timezone
# from .telebot import send_telegram
from datetime import datetime
# from .send_email import send_email


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
            basket_elems = basket.basketelem_set.all()
            context = str(len(basket_elems))
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
        basket_list = basket.basketelem_set.all()
        final_sum = final_sum_calc(basket)
        basket_set = loader.render_to_string(
            'shop/basket_input.html',
            {
                'basket_list': basket_list,
                'count_basket_elem': len(basket_list),
                'final_sum': final_sum,
            }
        )

        output_data = {
            'basket_set': basket_set,
        }
        return JsonResponse(output_data)


def delete_from_basket(request):
    if request.method == 'GET':
        elem_id = request.GET.get('elem_id')
        basket_elem = BasketElem.objects.get(id=elem_id)
        basket_elem.delete()
        basket = check_basket(request)
        basket_list = basket.basketelem_set.all()
        basket_count = len(basket_list)
        final_sum = final_sum_calc(basket)
        basket_set = loader.render_to_string(
            'shop/basket_input.html',
            {
                'basket_list': basket_list,
                'count_basket_elem': basket_count,
                'final_sum': final_sum,
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
        basket_list = basket.basketelem_set.all()
        basket_count = len(basket_list)

        final_sum = final_sum_calc(basket)
        basket_set = loader.render_to_string(
            'shop/basket_input.html',
            {
                'basket_list': basket_list,
                'count_basket_elem': basket_count,
                'final_sum': final_sum,
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
        final_sum = final_sum_calc(basket)
        if value == 'delivery2':
            final_sum += 250
        output_data = '{0} Руб.'.format(str(final_sum))
        return HttpResponse(output_data)


def final_sum_calc(basket):
    basket_list = basket.basketelem_set.all()
    final_sum = sum(i.sum for i in basket_list)
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