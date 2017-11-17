from django.conf.urls import url, include

from . import views

app_name = 'shop'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^change_filters$', views.change_filters, name='change_filters'),
    url(r'^change_filters_in_constructor$', views.change_filters_in_constructor, name='change_filters_in_constructor'),
    url(r'^select_product$', views.select_product, name='select_product'),
    url(r'^select_product_one_click$', views.select_product_one_click, name='select_product_one_click'),
    url(r'^add_to_basket$', views.add_to_basket, name='add_to_basket'),
    url(r'^delete_from_basket$', views.delete_from_basket, name='delete_from_basket'),
    url(r'^basket$', views.basket, name='basket'),
    url(r'^change_count_in_basket$', views.change_count_in_basket, name='change_count_in_basket'),
    url(r'^add_delivery$', views.add_delivery, name='add_delivery'),
    url(r'^search$', views.search, name='search'),
    url(r'^contact_pay$', views.contact_pay, name='contact_pay'),
    url(r'^change_count_one_click$', views.change_count_one_click, name='change_count_one_click'),
    url(r'^change_pack_one_click$', views.change_pack_one_click, name='change_pack_one_click'),
    url(r'^add_delivery_one_click$', views.add_delivery_one_click, name='add_delivery_one_click'),
    url(r'^make_order_one_click$', views.make_order_one_click, name='make_order_one_click'),
    url(r'^add_to_basket_in_constructor$', views.add_to_basket_in_constructor, name='add_to_basket_in_constructor'),
    url(r'^openconstructor$', views.openconstructor, name='openconstructor'),
    url(r'^change_pack_in_constructor$', views.change_pack_in_constructor, name='change_pack_in_constructor'),
    url(r'^delete_from_lego_flower$', views.delete_from_lego_flower, name='delete_from_lego_flower'),
    url(r'^add_to_basket_constructor$', views.add_to_basket_constructor, name='add_to_basket_constructor'),
    url(r'^call$', views.call, name='call'),
    url(r'^popoln$', views.popoln, name='popoln'),
    url(r'^popoln_one_click/(?P<one_click_id>[0-9]+)$', views.popoln_one_click, name='popoln_one_click'),
    url(r'^result$', views.res, name='result'),
    url(r'^success$', views.success, name='success'),
    url(r'^fail$', views.fail, name='fail'),
    # url(r'^res$', views.result_test, name='result_test'),
]
