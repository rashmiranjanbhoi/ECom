from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def about_page(request):
    return render(request, 'about/about.html')
