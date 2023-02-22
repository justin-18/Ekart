from django.contrib import admin

# Register your models here.
from store.models import Category,Products,Carts,Orders,Offers
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Carts)
admin.site.register(Orders)
admin.site.register(Offers)