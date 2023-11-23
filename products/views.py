from django.shortcuts import render
from django.http import HttpResponse
from products import views
from .models import Product,Category,cart
# Create your views here.
def home(request):
    
    contex={
        'featured_product':Product.objects.filter(featured=True)
    }
    return render(request,'home.html',contex)
def productdetails(request,slug):
    p_obj=Product.objects.get(slug=slug)
    
    return render(request,'productdetails.html',{'p_obj':p_obj})

def categorydetails(request,slug):
    c_obj=Category.objects.get(slug=slug)
   
    return render(request,'category.html',{'c_obj':c_obj})

def searchitem(request):
    if request.method == 'GET':
        search=request.GET.get('search')
        print(search)
        s_obj=Product.objects.filter(title__icontains=search)
       
        return render(request,'searchitem.html',{'s_obj':s_obj})
    return render(request,'searchitem.html')

def shoppingcart(request,slug):
    
        shopping_obj=Product.objects.get(slug=slug)
        
        
        cart_obj=cart.objects.create(product_name='hellow')
        cart_obj.save()
        print(cart_obj)
    
        return render(request,'shoppingcart.html',{'cart_obj':shopping_obj})