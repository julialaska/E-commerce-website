from django.shortcuts import render

# from eccomerce_website.product.models import Product, Category
from product.models import Product, Category


def frontpage(request):
    products = Product.objects.all()[0:6]

    return render(request, 'website_app/frontpage.html', {'products': products})


def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    active_category = request.GET.get('category', '')

    context = {
        'categories': categories,
        'products': products,
        'active_category': active_category
    }

    return render(request, 'website_app/shop.html', context)
