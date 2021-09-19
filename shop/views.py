from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Min, Max
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from shop.models import CarModel, CategoryModel, ColorModel


class CarsListView(ListView):
    template_name = 'shop-right-sidebar.html'
    paginate_by = 3

    def get_queryset(self):

        # context['recent_posts'] = self.object.category.cars.exclude(pk=self.object.pk)
        # context['recent_posts'] = CarModel.object.filter(category=self.object.category).exclude(pk=self.object.pk)

        qs = CarModel.objects.order_by('-pk')
        q = self.request.GET.get('q')
        cat = self.request.GET.get('cat')
        color = self.request.GET.get('color')
        sort = self.request.GET.get('sort')
        price = self.request.GET.get('price')

        if q:
            qs = qs.filter(title__icontains=q)

        if cat:
            qs = qs.filter(category_id=cat)

        if color:
            qs = qs.filter(colors__id=color)

        if price:
            price_from, price_to = price.split(';')
            qs = qs.filter(real_price__gte=price_from, real_price__lte=price_to)

        if sort:
            if sort == 'price':
                qs = qs.order_by('real_price')
            elif sort == '-price':
                qs = qs.order_by('real_price')

        return qs

    def get_context_data(self, **kwargs):
        context = super(CarsListView, self).get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()
        context['colors'] = ColorModel.objects.all()
        # context['price'] = PriceModel.objects.all()

        min_price, max_price = CarModel.objects.aggregate(
            Min('real_price'),
            Max('real_price')
        ).values()

        # context['min_price'], context['max_price'] = int(min_price), int(max_price)
        context['min_price'], context['max_price'] = list(
            map(
                int,
                CarModel.objects.aggregate(
                    Min('real_price'),
                    Max('real_price')
                ).values()
            )
        )

        return context


class CarDetailView(DetailView):
    template_name = 'blog-video-format.html'
    model = CarModel


class WishListListView(LoginRequiredMixin, ListView):
    template_name = 'wishlist.html'

    def get_queryset(self):
        return self.request.user.wishlist.all()


@login_required
def add_wishlist(request, pk):
    car = get_object_or_404(CarModel, pk=pk)
    user = request.user

    if user in car.wishlist.all():
        car.wishlist.remove(user)
    else:
        car.wishlist.add(user)

    return redirect(request.GET.get('next', '/'))


def add_to_cart(request, pk):
    cart = request.session.get('cart', [])

    if pk in cart:
        cart.remove(pk)
    else:
        cart.append(pk)

    request.session['cart'] = cart

    return redirect(request.GET.get('next', '/'))
