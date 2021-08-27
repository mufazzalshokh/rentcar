from django.urls import path

from shop.views import CarsListView

app_name = 'cars'

urlpatterns = [
    path('', CarsListView.as_view(), name='list'),
]
