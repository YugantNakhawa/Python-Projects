# admin.py

from django.contrib import admin
from .models import Cake, Order, Category, PinCode

class CakeAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories',)
    list_display = ('name', 'bakery_name')  # Add bakery_name to list_display

admin.site.register(Cake, CakeAdmin)  # Register Cake with the new admin class
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(PinCode)
