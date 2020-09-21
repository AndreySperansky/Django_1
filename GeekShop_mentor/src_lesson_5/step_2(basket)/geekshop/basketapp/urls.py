from django.conf.urls import url
from django.urls import path

import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    url(r'^$', basketapp.basket, name='view'),
    #url(r'^add/(?P<pk>\d+)/$', basketapp.basket_add, name='add'),
    path('add/<int:pk>/', basketapp.basket_add, name='add'),
    url(r'^remove/(?P<pk>\d+)/$', basketapp.basket_remove, name='remove'),
]

    