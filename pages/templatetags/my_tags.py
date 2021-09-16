from django import template

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
