from django.conf.urls import url

import mainapp.views as mainapp

# обязательно указывать для django 2.0
app_name = 'mainapp'

urlpatterns = [
    url(r'^$', mainapp.products, name='index'),
    url(r'^(\d+)/$', mainapp.products, name='category'),
    
]

    