from django.shortcuts import render,redirect
from shop.models import Product
from contact.forms import SubscriberForm
from django.contrib.auth.forms import UserCreationForm
from .forms import createUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home_page(request):
    products = Product.objects.all()[:8]
    forms = SubscriberForm()
    if request.method == 'POST':
        forms = SubscriberForm(request.POST)
        if forms.is_valid():
            forms.save()
    context = {
        'products': products,
        'forms': forms
    }
    return render(request, 'home.html', context)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form=createUserForm()
        if request.method == 'POST':
            form = createUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request,'Account is created by ' + user)

                return redirect('login')


        context ={'form':form}
        return render(request, 'registerr.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'Username and Password is Incorrect')      
        context={}
        return render(request, 'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')