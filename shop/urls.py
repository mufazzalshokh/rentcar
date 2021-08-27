from django.urls import path

from shop.views import CarsListView

app_name = 'cars'

urlpatterns = [
    # path('<int:pk>/', CarDetailView.as_view(), name='detail'),
    path('', CarsListView.as_view(), name='list'),
]
