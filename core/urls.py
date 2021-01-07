from django.urls import path
from .views import (
    HomeView, 
    CheckOutView,
    ItemDetailView,
    add_to_cart, 
    remove_from_cart,
    OrderSummary,
    remove_single_item_from_cart,
    )


app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='item_list'),
    path('checkout/', CheckOutView.as_view(), name='checkout'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add_to_cart/<slug>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<slug>/', remove_from_cart, name='remove_from_cart'),
    path('order_summary/', OrderSummary.as_view(), name='order_summary'),
    path('remove_single_item_from_cart/<slug>/', remove_single_item_from_cart, name='remove_single_item_from_cart'),
]
