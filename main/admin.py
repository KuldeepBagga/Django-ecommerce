from django import forms
from django.contrib import admin
from mptt.admin import MPTTModelAdmin,DraggableMPTTAdmin

from .models import Menu,Product

class MenuAdmin(MPTTModelAdmin):
    mptt_indent_field = "menu_name"
    list_display = ('menu_name',"status","parent_menu")
    list_display_links = ('menu_name',)
        
admin.site.register(Menu,MenuAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=["product_name","status","product_price","product_image","parent_menu","short_description","long_description","featured_product","popular_product"]

admin.site.register(Product,ProductAdmin)    