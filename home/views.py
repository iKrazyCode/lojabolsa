from django.shortcuts import render, HttpResponse
from .utils.api import NuvemShopApi

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def monte(request):
    products_id = NuvemShopApi.get_products_id(products_urls=[
         'https://enepta.lojavirtualnuvem.com.br/produtos/carro-importado/',
         'https://enepta.lojavirtualnuvem.com.br/produtos/jaqueta-de-couro/'
    ])

    products_list_variants = []
    for prod_url, prod_id in products_id:
        products_list_variants.append({'variant_id': prod_id, 'quantity': 1})

    data = {
        'contact_name': 'teste',
        'contact_lastname': 'testedg',
        'contact_email': 'teste@gmail.com',
        'payment_status': 'unpaid',
        'products': products_list_variants,
    }
    # cart = NuvemShopApi.post('/draft_orders/', data=data)

    # print(cart)

    return render(request, 'home/monte.html')