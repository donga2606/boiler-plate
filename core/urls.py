from django.urls import path
from .views import (
    HomeView, 
    check_out, 
    ItemDetailView,
    add_to_cart, remove_from_cart,
    )


app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='item_list'),
    path('checkout/', check_out, name='checkout'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add_to_cart/<slug>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<slug>/', remove_from_cart, name='remove_from_cart'),
]
