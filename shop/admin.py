from django.contrib import admin
from .models import Product, Category, Basket, BasketElem, Package
from django.db import models
from django.forms import CheckboxSelectMultiple


class ForModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Basket)
admin.site.register(BasketElem)
