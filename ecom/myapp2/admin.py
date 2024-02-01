from django.contrib import admin
from .models import User, Product, Order


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number']
    ordering = ['name', '-email']
    list_filter = ['name', 'email']
    search_fields = ['name', 'email']
    search_help_text = 'Поиск по полю Имя пользователя (name), почта (email)'
    fields = ['name', 'email', 'phone_number', 'address', 'reg_date']
    readonly_fields = ['reg_date']
    
    

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity']
    ordering = ['name', '-quantity']
    list_filter = ['added_date', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукт (description)'
    fields = ['name', 'description', 'category', 'price', 'added_date', 'image']
    readonly_fields = ['added_date']
    
    
admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
