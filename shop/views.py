from django.views.generic import ListView

from shop.models import CarModel


class CarsListView(ListView):
    template_name = 'shop-right-sidebar.html'
    queryset = CarModel.objects.order_by('-pk')
