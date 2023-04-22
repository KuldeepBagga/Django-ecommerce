from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from main.models import Menu , Product

# Create your views here.
def home(request):
    global menu_list
    global child_menu
#    #menu_list=Menu.objects.all()
    menu_list=Menu.objects.filter(status="active",parent_menu=None)
    child_menu=Menu.objects.filter(status="active",parent_menu__isnull=False)
    template = loader.get_template("index.html")    
    context = {
        "title": "Home Page",
        "menu":menu_list,
        "child_menu":child_menu
    }
    return HttpResponse(template.render(context, request))

def category(request,id):
    product_list=Product.objects.filter(parent_menu=id)
    template = loader.get_template("category.html")
    menu_listss=Menu.objects.filter(id=id)
    context = {
       "title":menu_listss,
       "product_list":product_list,
       "menu":menu_list,
       "child_menu":child_menu,
    }
    return HttpResponse(template.render(context, request))

def products(request,id):
    template=loader.get_template("product-details.html")
    products=Product.objects.filter(id=id)
    context={
        'product':products,
        "menu":menu_list,
        "child_menu":child_menu,
    }
    return HttpResponse(template.render(context,request))