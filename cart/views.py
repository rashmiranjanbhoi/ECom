from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def cart_page(request):
    return render(request, 'cart/cart.html')
@login_required(login_url='login')
def checkout(request):
    return render(request, 'cart/checkout.html')
