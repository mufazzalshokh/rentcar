from django import template
from django.db.models import Sum

from pages.utils import get_cart_length
from shop.models import CarModel

register = template.Library()


@register.simple_tag
def get_price_url(request, x):
    price = request.GET.get('price')
    if price:
        return price.split(';')[x]
    return 'null'


@register.simple_tag()
def get_lang_url(request, lang):
    # it is standart and easier for 2 alphabet

    # url = request.path
    # url = '/' + lang + url[3:]
    # return url

    # return '/' + lang + request.path

    # universal for 3 alphabet

    url = request.path.split('/')
    url[1] = lang
    url = '/'.join(url)
    return url


@register.filter
def in_wishlist(car, request):
    return request.user in car.wishlist.all()


@register.filter
def in_cart(car, request):
    return car.pk in request.session.get('cart', [])


@register.simple_tag
def cart_count(request):
    # cart = request.session.get('cart', [])
    return get_cart_length(request)


@register.simple_tag
def cart_price(request):
    if get_cart_length(request) == 0:
        return 0

    return CarModel.get_from_cart(request).aggregate(Sum('real_price'))['real_price__sum']
