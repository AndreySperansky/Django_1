import datetime, random, os, json
from django.shortcuts import render, get_object_or_404
from mainapp.models import ProductCategory, Product
from basketapp.models import Basket

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


JSON_PATH = 'mainapp/json'


def loadFromJSON(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


def getBasket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []

        
def getHotProduct():
    products = Product.objects.filter(is_active=True, category__is_active=True)
    
    return random.sample(list(products), 1)[0]
    
    
def getSameProducts(hot_product):
    same_products = Product.objects.filter(category=hot_product.category, is_active=True).exclude(pk=hot_product.pk)[:3]
    
    return same_products
        

        
def main(request):
    title = 'главная'  
    products = Product.objects.filter(is_active=True, category__is_active=True)[:3]
    
    content = {
        'title': title,
        'products': products,
        'basket': getBasket(request.user),
    }
    
    return render(request, 'mainapp/index.html', content)
    

def products(request, pk=None, page=1):
    title = 'продукты'
    links_menu = ProductCategory.objects.filter(is_active=True)
    basket = getBasket(request.user)
           
    if pk:
        if pk == '0':
            category = {
                'pk': 0,
                'name': 'все'
            }
            products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            # все объекты
            products = Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by('price')

        # экземпляр класса Paginator 2- сколько объектов на странице
        paginator = Paginator(products, 2)
        try:
            # получение объектов нужной сраницы
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            # последняя страница
            products_paginator = paginator.page(paginator.num_pages)

        print('products----->', type(products))
        print('products_paginator----->', type(products_paginator))
        
        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products_paginator,
            'basket': basket,
        }
        
        return render(request, 'mainapp/products_list.html', content)
    
    hot_product = getHotProduct()
    same_products = getSameProducts(hot_product)
    
    content = {
        'title': title,
        'links_menu': links_menu, 
        'hot_product': hot_product,
        'same_products': same_products,
        'basket': basket,
    }
    
    return render(request, 'mainapp/products.html', content)
    
    
def product(request, pk):
    title = 'продукты'
    links_menu = ProductCategory.objects.filter(is_active=True)

    product = get_object_or_404(Product, pk=pk)
    
    content = {
        'title': title, 
        'links_menu': links_menu, 
        'product': product, 
        'basket': getBasket(request.user),
    }
    return render(request, 'mainapp/product.html', content)
    

def contact(request):
    title = 'о нас'
    
    locations = loadFromJSON('contact__locations')
    
    content = {
        'title': title,
        'locations': locations,
        'basket': getBasket(request.user),
    }
    
    return render(request, 'mainapp/contact.html', content)
    
    
