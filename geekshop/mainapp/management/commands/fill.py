''' ЗАПОЛНЕНИЕ БАЗЫ '''

from django.core.management import BaseCommand
from geekshop.settings import BASE_DIR
from mainapp.models import ProductCategory, Product
import os
import json

def load_json(file_name):
    category_path_file = os.path.join(BASE_DIR, file_name + '.json')
    # category_path_file = os.path.join('mainapp/json', file_name + '.json')
    
    with open(category_path_file, encoding = 'utf-8') as json_file:
        return json.load(json_file)
    


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        categories = load_json('categories')
        print(categories)
        
        ProductCategory.objects.all().delete()
        
##################################################################################
        cats_dict = dict()
        for cat in categories:
            #ProductCategory.objects.create(**cat)
    #    или так
            
            new_cat = ProductCategory(**cat)
            new_cat.save()
            cats_dict[cat['name']] = new_cat.id
   
#################################################################################
        products = load_json('products')
        Product.objects.oll().delete()
        
        for product in products:
            #category_item = ProductCategory.objects.get(name=product['category'])
            #product['category'] = category_item
            product['category_id'] = cats_dict[product['category']]
            new_prod = Product(**product)
            new_prod.save()
        


   
   
    
        
    # def handle(self, *args, **kwargs):
        # ProductCategory.objects.create(
        #     name = 'Шкафы'
        # )
        # categories = ProductCategory.objects.all()
        # print(categories)



        