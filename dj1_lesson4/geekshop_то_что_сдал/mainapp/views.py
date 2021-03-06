from django.shortcuts import render
import os
import json
import datetime

# Create your views here.
from geekshop.settings import BASE_DIR
from mainapp.models import Product



def main (request):
    products = Product.objects.all()[:4]
    context = { 'title': 'title', 'products': products }
    return render(request, 'mainapp/index.html', context)

def products (request):
    title = 'продукты'
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]

    same_products = []
    products_file_path = os.path.join(BASE_DIR, 'products.json')
    if os.path.exists(products_file_path):                          # is file exists check up
        with open(products_file_path, encoding = 'utf-8') as products_file:             # open file
            same_products = json.loads(products_file.read())
    # context = { 'title': 'продукты', 'same_product': same_products, 'submenu': submenu }
    context = { 'title': title, 'links_menu': links_menu, 'same_products': same_products }
    
    return render(request, 'mainapp/products.html', context)

# def contact (request):
#     return render(request, 'mainapp/contact.html')

# вариант функции cocntact  с JSON
def contact (request):
    title = 'о нас'
    visit_date = datetime.datetime.now()
    locations = []
    contacts_file_path = os.path.join(BASE_DIR, 'contacts.json')
    if os.path.exists(contacts_file_path):
        with open(contacts_file_path, encoding = 'utf-8') as contacts_file:
            locations = json.loads(contacts_file.read())
    content = {'title': title, 'visit_date': visit_date, 'locations': locations}
    return render(request, 'mainapp/contact.html', content)




