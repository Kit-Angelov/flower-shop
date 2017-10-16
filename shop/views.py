from django.shortcuts import render, get_object_or_404, render_to_response, get_list_or_404
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import Category, Product, Basket, BasketElem
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import uuid
# from .forms import ProductsSearchForm
# from .telebot import send_telegram
# from datetime import datetime
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
        product_html = loader.render_to_string(
            'shop/infoflower_input.html',
            {
                'product_info': product,
            }
        )
        output_data = {
            'product_info': product_html,
        }
        return JsonResponse(output_data)


def search(request):
    pass


def call(request):
    pass


def add_to_basket(request):
    basket = check_basket(request)
    if request.method == 'GET':
        print('REQUESTPOST', request.POST)
        product_id = int(request.GET.get('product_id'))
        flower_count = int(request.GET.get('flower_count'))

        product = Product.objects.get(id=product_id)
        basket_elem = BasketElem(product=product, basket=basket, count=flower_count)
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