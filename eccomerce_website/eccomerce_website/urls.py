from django.contrib import admin
from django.urls import path

from websiteapp.views import frontpage, shop, signup
from product.views import product
from cart.views import add_to_cart

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product, name='product'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('admin/', admin.site.urls),
]
