from django.contrib import admin
from django.utils.html import format_html
from .models import Menu,Product

class MenuAdmin(admin.ModelAdmin):
    list_display=["menu_name","status","parent_menu"]

admin.site.register(Menu,MenuAdmin)
    
class ProductAdmin(admin.ModelAdmin):
    list_display=["product_name","status","product_price","product_image","parent_menu","featured_product","popular_product"]

admin.site.register(Product,ProductAdmin)

