from django.views.generic import ListView

from shop.models import CarModel, CategoryModel


class CarsListView(ListView):
    template_name = 'shop-right-sidebar.html'
    paginate_by = 3

    def get_queryset(self):

        # context['recent_posts'] = self.object.category.cars.exclude(pk=self.object.pk)
        # context['recent_posts'] = CarModel.object.filter(category=self.object.category).exclude(pk=self.object.pk)

        qs = CarModel.objects.order_by('-pk')
        q = self.request.GET.get('q')
        cat = self.request.GET.get('cat')

        if q:
            qs = qs.filter(title__icontains=q)

        if cat:
            qs = qs.filter(category_id=cat)

        return qs

    def get_context_data(self, **kwargs):
        context = super(CarsListView, self).get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()
        # context['price'] = PriceModel.objects.all()
        # context['color'] = ColorModel.objects.all()

        return context
