"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
import mainapp.views as mainapp
from geekshop import settings

urlpatterns = [
    
    path('admin/', admin.site.urls),
    
    path( '' , mainapp.main, name='main'),           # 127.0.0.1:8000
    path( 'products/' , mainapp.products, name='products'),  # 127.0.0.1:8000/products/
    path( 'contact/' , mainapp.contact, name='contacts'),       # 127.0.0.1:8000/contact/
    
    path( 'products/all/' , mainapp.products, name='products_all'),
    path( 'products/home/' , mainapp.products, name='products_home'),
    path( 'products/office/' , mainapp.products, name='products_office'),
    path( 'products/modern/' , mainapp.products, name='products_modern'),
    path( 'products/classic/' , mainapp.products, name='products_classic'),
]


# URLs для media

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


