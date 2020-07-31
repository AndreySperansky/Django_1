from django.shortcuts import render
import os
import json
import datetime
from geekshop.settings import BASE_DIR
from mainapp.models import ProductCategory, Product



def main (request):
    products = Product.objects.all()[:4]
    context = { 'title': 'title', 'products': products }
    return render(request, 'mainapp/index.html', context)

def products (request, pk = None):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    same_products = Product.objects.all()
    
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




