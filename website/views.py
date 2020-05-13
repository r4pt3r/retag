from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name':'Retag'})

def shop(request):
    return render(request, 'shop.html', {'name':'Retag'})

def wishlist(request):
    return render(request, 'wishlist.html', {'name':'Retag'})

def product(request):
    return render(request, 'product-single.html', {'name':'Retag'})

def cart(request):
    return render(request, 'cart.html', {'name':'Retag'})

def checkout(request):
    return render(request, 'checkout.html', {'name':'Retag'})