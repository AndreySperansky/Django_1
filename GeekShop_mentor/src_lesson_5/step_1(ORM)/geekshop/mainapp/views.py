from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render, get_object_or_404
import datetime
from .models import ProductCategory, Product


def main(request):
    title = 'главная'
    
    products = Product.objects.all()[:3]
    
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)
    

def products(request, pk=None):
    print(pk)
    
    title = 'продукты'
    links_menu = ProductCategory.objects.all()
            
    if pk:
        if pk == '0':
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            # try:
            #     category = ProductCategory.objects.get(pk=pk)
            # except ObjectDoesNotExist:
            #     raise Http404

            products = Product.objects.filter(category__pk=pk).order_by('price')
        
        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products, 
        }
        
        return render(request, 'mainapp/products_list.html', content)
    
    same_products = Product.objects.all()[3:5]
    
    content = {
        'title': title,
        'links_menu': links_menu, 
        'same_products': same_products
    }
    
    return render(request, 'mainapp/products.html', content)
    

def contact(request):
    title = 'о нас'
    visit_date = datetime.datetime.now()
    locations = [
        {
            'city': 'Москва',
            'phone': '+7-888-888-8888',
            'email': 'info@geekshop.ru',
            'address': 'В пределах МКАД',
        },
        {
            'city': 'Екатеринбург',
            'phone': '+7-777-777-7777',
            'email': 'info_yekaterinburg@geekshop.ru',
            'address': 'Близко к центру',
        },
        {
            'city': 'Владивосток',
            'phone': '+7-999-999-9999',
            'email': 'info_vladivostok@geekshop.ru',
            'address': 'Близко к океану',
        },
    ]
    content = {'title': title, 'visit_date':visit_date, 'locations': locations}
    return render(request, 'mainapp/contact.html', content)
    
    
