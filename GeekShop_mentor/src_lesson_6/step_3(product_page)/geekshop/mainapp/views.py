from django.shortcuts import render, get_object_or_404
import datetime
from .models import ProductCategory, Product
from basketapp.models import Basket
import random, os, json


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
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]
    
    
def getSameProducts(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    
    return same_products
        

        
def main(request):
    title = 'главная'  
    products = Product.objects.all()[:3]
    
    content = {
        'title': title,
        'products': products,
        'basket': getBasket(request.user),
    }
    
    return render(request, 'mainapp/index.html', content)
    

def products(request, pk=None):   
    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    basket = getBasket(request.user)
           
    if pk:
        if pk == '0':
            category = {'name': 'все'}
            products = Product.objects.all().order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')
        
        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
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
    
    content = {
        'title': title, 
        'links_menu': ProductCategory.objects.all(), 
        'product': get_object_or_404(Product, pk=pk), 
        'basket': getBasket(request.user),
    }
	
    return render(request, 'mainapp/product.html', content)
    

def contact(request):
    title = 'о нас'
    visit_date = datetime.datetime.now()
    
    locations = loadFromJSON('contact__locations')
    
    content = {
        'title': title,
        'visit_date':visit_date, 
        'locations': locations,
        'basket': getBasket(request.user),
    }
    
    return render(request, 'mainapp/contact.html', content)
    
    
