from django.contrib import admin
from .models import Basket


# admin.site.register(Basket)

# раширение стандартной админки
class BasketAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'user']


admin.site.register(Basket, BasketAdmin)
