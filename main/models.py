from django.db import models
from ckeditor.fields import RichTextField
from django import forms

class Menu(models.Model):
    menu_name=models.CharField(max_length=50,null=False)
    status=models.CharField(max_length=20,choices=[("active","Active"),("disable","Disable")],default="active")
    parent_menu=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.menu_name
    
class Product(models.Model):
    product_name=models.CharField(max_length=100)
    status=models.CharField(max_length=20,choices=[("active","Active"),("disable","Disable")],default="active")
    product_price=models.CharField(max_length=20)
    product_image=models.ImageField(max_length=50,upload_to="products")
    parent_menu=models.ForeignKey(Menu, on_delete=models.CASCADE)
    short_description=RichTextField(blank=True,null=True)
    long_description=RichTextField(blank=True,null=True)
    featured_product=models.CharField(max_length=10,null=True,blank=True,choices=[("1","Yes"),("0","No")])
    popular_product=models.CharField(max_length=10,null=True,blank=True,choices=[("1","Yes"),("0","No")])
    