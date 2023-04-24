from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from main.models import Menu , Product

# Create your views here.
def home(request):
    global menu_list
    menu_list=Menu.objects.all()
    template = loader.get_template("index.html")    
    context = {
        "title": "Home Page",
        "menu":menu_list
    }
    return HttpResponse(template.render(context, request))

def category(request,slug):
    product_list=Product.objects.select_related("parent_menu").filter()
    print(product_list)
    #product_list=Product.objects.all().select_related("parent_menu")
    template = loader.get_template("category.html")
    context = {
       "product_list":product_list,
       "menu":menu_list,
    }
    return HttpResponse(template.render(context, request))

def products(request,id):
    template=loader.get_template("product-details.html")
    products=Product.objects.filter(id=id)
    context={
        'product':products,
        "menu":menu_list,
    }
    return HttpResponse(template.render(context,request))