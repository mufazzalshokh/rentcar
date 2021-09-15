from django import template

register = template.Library()


@register.simple_tag
def get_price_url(request, x):
    price = request.GET.get('price')
    if price:
        return price.split(';')[x]
    return 'null'
