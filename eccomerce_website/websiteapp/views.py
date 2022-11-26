from django.shortcuts import render

# from eccomerce_website.product.models import Product
from product.models import Product


def frontpage(request):
    products = Product.objects.all()[0:8]
    return render(request, 'website_app/frontpage.html', {'products': products})
