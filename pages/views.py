from django.urls import reverse
from django.views.generic import CreateView, TemplateView

from blog.models import PostModel
from pages.forms import ContactModelForm
from shop.models import CarModel


class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = PostModel.objects.order_by('-pk')[:4]
        context['products'] = CarModel.objects.order_by('-pk')[:4]

        return context


class ContactCreateView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm

    def get_success_url(self):
        return reverse('pages:contact')


class AboutTemplateView(TemplateView):
    template_name = 'about.html'
