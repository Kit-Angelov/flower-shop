from django.conf.urls import url, include

from . import views

app_name = 'shop'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^change_filters$', views.change_filters, name='change_filters'),
    url(r'^select_product$', views.select_product, name='select_product'),
    url(r'^add_to_basket$', views.add_to_basket, name='add_to_basket'),
    # url(r'^catalog/(?P<category_id>[0-9]+)/$', views.catalog, name='catalog'),
    # url(r'^product/(?P<product_id>[0-9]+)/$', views.product_detail, name='product'),
    # url(r'^basket/$', views.basket, name='basket'),
    # url(r'^basket_closed/$', views.basket_closed, name='basket_closed'),
    # url(r'^delete_elem_basket_closed/(?P<id>[0-9]+)$', views.delete_order_elem_basket_closed, name='delete_elem_basket_closed'),
    # url(r'^delete_elem_basket/(?P<id>[0-9]+)$', views.delete_order_elem_basket, name='delete_elem_basket'),
    # url(r'^search/$', views.search, name='search'),
    # url(r'add_to_basket/$', views.add_to_basket, name='add_to_basket'),
    # url(r'call/$', views.call, name='call'),
    # url(r'^closed_order/$', views.closed_order, name='closed_order'),
]
