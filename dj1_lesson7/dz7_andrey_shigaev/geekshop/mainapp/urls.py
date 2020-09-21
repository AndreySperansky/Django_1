from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='index'),   # все товары
    path('category/<int:pk>/', mainapp.products, name='category'),  # категории товаров
    path('product/<int:pk>/', mainapp.product, name='product'),  #
    
]
