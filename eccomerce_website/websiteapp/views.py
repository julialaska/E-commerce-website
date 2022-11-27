from django.shortcuts import render

# from eccomerce_website.product.models import Product
from product.models import Product


def frontpage(request):
    products = Product.objects.all()[0:6]

    return render(request, 'website_app/frontpage.html', {'products': products})


def shop(request):
    products = Product.objects.all()

    return render(request, 'website_app/shop.html', {'products': products})
