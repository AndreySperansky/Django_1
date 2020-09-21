from django.conf.urls import url, include
from django.contrib import admin
import mainapp.views as mainapp

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', mainapp.main, name='main'),
    url(r'^products/', include('mainapp.urls', namespace='products')),
    url(r'^auth/', include('authapp.urls', namespace='auth')),
    url(r'^contact/', mainapp.contact, name='contact'),
    
    
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
