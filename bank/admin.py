from django.contrib import admin

# Register your models here.
from .models import FoodProduct, Order

admin.site.register(FoodProduct)
admin.site.register(Order)