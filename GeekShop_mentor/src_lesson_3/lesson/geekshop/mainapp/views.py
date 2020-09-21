from django.shortcuts import render
import datetime
from .models import Product


def main(request):
    title = 'главная'
    products = [
        {
            'name': 'Отличный стул',
            'desc': 'Расположитесь комфортно.',
            'image_src': 'product-1.jpg',
            'image_href': '/product/1/',
            'alt': 'продукт 1'
        },
        {
            'name': 'Стул повышенного качества', 
            'desc': 'Не оторваться.',
            'image_src': 'product-2.jpg',
            'image_href': '/product/2/',
            'alt': 'продукт 2'
        },
    ]
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)
    

def products(request):
    title = 'продукты'
    links_menu = [
        {'href': '/products/0/', 'name': 'все'},
        {'href': '/products/1/', 'name': 'дом'},
        {'href': '/products/2/', 'name': 'офис'},
        {'href': '/products/3/', 'name': 'модерн'},
        {'href': '/products/4/', 'name': 'классика'},
    ]
    same_products = Product.objects.all()
    content = {'title': title, 'links_menu': links_menu, 'same_products': same_products}
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
    
    
