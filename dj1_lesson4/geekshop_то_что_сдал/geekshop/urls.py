
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import include
import mainapp.views as mainapp
from geekshop import settings

urlpatterns = [
    
    path('admin/', admin.site.urls),
    
    path( 'auth/' , include( 'authapp.urls' , namespace= 'auth' )),
    
    path( '' , mainapp.main, name='main'),           # 127.0.0.1:8000
    path( 'products/', mainapp.products, name='products'),  # 127.0.0.1:8000/products/
    path( 'contact/', mainapp.contact, name='contacts'),       # 127.0.0.1:8000/contact/
    
    path( 'products/all/' , mainapp.products, name='products_all'),
    path( 'products/home/' , mainapp.products, name='products_home'),
    path( 'products/office/' , mainapp.products, name='products_office'),
    path( 'products/modern/' , mainapp.products, name='products_modern'),
    path( 'products/classic/' , mainapp.products, name='products_classic'),
]


# URLs для media

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



