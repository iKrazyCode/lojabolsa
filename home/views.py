from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def monte(request):
    return render(request, 'home/monte.html')