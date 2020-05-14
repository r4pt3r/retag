from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Reviews
# Create your views here.

def home(request):
    return render(request, 'home.html', {'name':'Retag'})

def shop(request):
    return render(request, 'shop.html', {'name':'Retag'})

def wishlist(request):
    return render(request, 'wishlist.html', {'name':'Retag'})

def product(request):

    if request.method == 'POST':
        stars = request.POST['star']
        comments = request.POST['comment']
        reviews = Reviews(stars=stars, comments=comments)
        reviews.save()
        return redirect('/product-single')

    else:
        reviews = Reviews.objects.all()
        return render(request, 'product-single.html', {'reviews':reviews})

def cart(request):
    return render(request, 'cart.html', {'name':'Retag'})

def checkout(request):
    return render(request, 'checkout.html', {'name':'Retag'})