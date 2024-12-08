from django.shortcuts import render, HttpResponse
from .utils.api import NuvemShopApi

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def monte(request):
    cart = NuvemShopApi.post('/draft/')
    
    return render(request, 'home/monte.html')