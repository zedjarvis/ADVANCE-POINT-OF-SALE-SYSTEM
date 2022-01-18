from django.contrib import admin
from .models import Store, Category, Item, Sale, Payment, DeadStock, Stock

# Register your models here.
admin.site.register(Store)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Sale)
admin.site.register(Payment)
admin.site.register(DeadStock)
admin.site.register(Stock)
