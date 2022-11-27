from django.contrib import admin
from django.urls import path

from websiteapp.views import frontpage, shop

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('shop/', shop, name='shop'),
    path('admin/', admin.site.urls),
]
