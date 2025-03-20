from django.contrib import admin

from shop.models import Category, Product, Images, Customer

# Register your models here.


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Images)
admin.site.register(Customer)