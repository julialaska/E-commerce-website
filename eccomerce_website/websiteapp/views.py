from django.contrib.auth import login
from django.db.models import Q
from django.shortcuts import render, redirect

from product.models import Product, Category

from .forms import SignupForm


def frontpage(request):
    products = Product.objects.all()[0:8]

    return render(request, 'website_app/frontpage.html', {'products': products})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('/')
    else:
        form = SignupForm()

    return render(request, 'website_app/signup.html', {'form': form})


def login_old(request):
    return render(request, 'website_app/login.html')


def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    active_category = request.GET.get('category', '')

    if active_category:
        products = products.filter(category__slug=active_category)

    query = request.GET.get('query', '')

    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context = {
        'categories': categories,
        'products': products,
        'active_category': active_category
    }

    return render(request, 'website_app/shop.html', context)
