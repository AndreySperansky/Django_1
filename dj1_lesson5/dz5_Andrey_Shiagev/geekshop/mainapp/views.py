from basketapp.models import Basket
from django.shortcuts import render
import datetime
from .models import ProductCategory, Product
from django.shortcuts import get_object_or_404


def main(request):
    title = 'главная'
    
    products = Product.objects.all()[:4]
    
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)
    

def products(request, pk=None):
  
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user = request.user)

    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    content = {
        'title'     : title,
        'links_menu': links_menu,
        'basket'    : basket,
    }

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk = pk)
            products = Product.objects.filter(category__pk = pk).order_by('price')
            
        content['category'] = category
        content['products'] = products
        
    
        return render(request, 'mainapp/products_list.html', content)

    same_products = Product.objects.all()[3:5]
    content['same_products'] = same_products
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
    
    
