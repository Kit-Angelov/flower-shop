from shop.models import Basket


def _counts(request):
    try:
        basket = Basket.objects.get(guid=request.session['guid'])
        basket_elems = basket.basketelem_set.all()
        return {'count': str(len(basket_elems))}
    except Exception as e:
        print('EXEPTION', e)
        return {'count': str(0)}
