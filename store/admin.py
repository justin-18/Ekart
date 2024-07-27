from django.contrib import admin

from store.models import Category,Products,Offers,Carts,Orders,Reviews
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Offers)
admin.site.register(Reviews)