from django.shortcuts import render

# Create your views here.

def main (request):
    context = {
        'title': 'главная'
    }
    return render(request, 'mainapp/index.html', context)

def products (request):
    same_products = []
    submenu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    context = {
        'title': 'продукты',
        'same_product': same_products,
        'submenu': submenu
    }
    return render(request, 'mainapp/products.html', context)

def contact (request):
    return render(request, 'mainapp/contact.html')

