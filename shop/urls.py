from django.urls import path

from shop.views import CarsListView, CarDetailView, WishListListView, add_wishlist, add_to_cart

app_name = 'cars'

urlpatterns = [
    path('<int:pk>/', CarDetailView.as_view(), name='detail'),
    path('wishlist', WishListListView.as_view(), name='wishlist'),
    path('wishlist/<int:pk>', add_wishlist, name='add_wishlist'),
    path('add_to_cart/<int:pk>', add_to_cart, name='add_to_cart'),
    path('', CarsListView.as_view(), name='list'),
]
