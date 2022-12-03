from django.shortcuts import render

from product.models import Product


def product(request, slug):
    product = Product.objects.get(slug=slug)

    return render(request, 'product/product.html', {'product': product})
