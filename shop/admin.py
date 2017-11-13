from django.contrib import admin
from .models import Product, Category, Basket, BasketElem, Package, SalePromo, Attribute, Constructor, Call
from django.db import models
from django.forms import CheckboxSelectMultiple


class BasketElemInline(admin.TabularInline):
     model = BasketElem


class BasketAdmin(admin.ModelAdmin):
    model = Basket
    list_display = ['phone', 'name', 'date', 'sum']
    search_fields = ['name',]
    list_filter = ['date', 'complite']
    inlines = (BasketElemInline,)


class BasketElemAdmin(admin.ModelAdmin):
    list_display = ['basket', 'count', 'sum', 'product']
    raw_id_fields = ['basket',]


class ForModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Basket, BasketAdmin)
admin.site.register(BasketElem, BasketElemAdmin)
admin.site.register(Package)
admin.site.register(SalePromo)
admin.site.register(Attribute)
admin.site.register(Constructor)
admin.site.register(Call)
