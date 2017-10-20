from django.conf.urls import url, include

from . import views

app_name = 'shop'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^change_filters$', views.change_filters, name='change_filters'),
    url(r'^select_product$', views.select_product, name='select_product'),
    url(r'^add_to_basket$', views.add_to_basket, name='add_to_basket'),
    url(r'^delete_from_basket$', views.delete_from_basket, name='delete_from_basket'),
    url(r'^basket$', views.basket, name='basket'),
    url(r'^change_count_in_basket$', views.change_count_in_basket, name='change_count_in_basket'),
    url(r'^add_delivery$', views.add_delivery, name='add_delivery'),
    url(r'^search$', views.search, name='search'),
    # url(r'^get_package_list$', views.get_package_list, name='get_package_list'),
]
