from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, OrderItem, Order
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages


class HomeView(ListView):
    template_name = 'home.html'
    model = Item
    context_object_name = 'items'

# def home(request):
#     items = Item.objects.all()
#     context = {'items': items}
#     return render(request, 'home.html', context)

@login_required
def check_out(request):
    return render(request, 'checkout.html')


# def product(request):
#     items = Item.objects.all()
#     context = {'items': items}
#     return render(request, 'product.html', context)

class ItemDetailView(DetailView):
    template_name = 'product.html'
    context_object_name = 'item'
    model = Item

@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    user = request.user
    order_item, created = OrderItem.objects.get_or_create(
        ordered=False,
        user=user,
        item=item,
    )

    order_qs = Order.objects.filter(user=user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if not created:
            order_item.quantity += 1
            order_item.save()
            messages.info(request, 'This item quantity was update!')
        else:
            order.items.add(order_item)
            messages.info(request, 'This item was added into your cart!')
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, 'This item was added into your cart!')

    return redirect('core:product', slug=slug)


@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    user = request.user
    order_item_qs = OrderItem.objects.filter(
        item=item,
        ordered=False,
        user=user,
        )
    if not order_item_qs.exists():
        messages.info(request, 'You do not have this item in cart!')
    else:
        order_item = order_item_qs[0]
        order = Order.objects.get(
            user=user,
            ordered=False,
        )
        order.items.remove(order_item)
        order_item.delete()
        messages.info(request, 'Successful remove item from cart')

    return redirect('core:product', slug=slug)
