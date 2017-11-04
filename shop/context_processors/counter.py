from shop.models import Basket


def _counts(request):
    try:
        basket = Basket.objects.get(guid=request.session['guid'])
        basket_elems = basket.basketelem_set.all().filter(constructor_child=False)
        constructor_elems = basket.constructor_set.all().filter(build=True)
        count = str(len(basket_elems) + len(constructor_elems))
        return {'count': count}
    except Exception as e:
        print('EXEPTION', e)
        return {'count': str(0)}
