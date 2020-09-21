from django.urls import path
from .views import products_list

app_name = 'products'

urlpatterns = [
    path('list/', products_list, name='product_list')
]