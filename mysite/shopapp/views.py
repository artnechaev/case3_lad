from django.shortcuts import render

from .models import Product, Order


def index(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'shopapp/index.html', context)


def products_list(request):
    products = Product.objects.all()
    context = {
        'title': 'Список продуктов',
        'products': products,
    }
    return render(request, 'shopapp/products.html', context)


def orders_list(request):
    orders = Order.objects.all().prefetch_related('products')
    # products =
    context = {
        'title': 'Список заказов',
        'orders': orders,
    }
    return render(request, 'shopapp/orders.html', context)
