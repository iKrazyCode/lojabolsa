from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse

from .utils.api import NuvemShopApi
from .models import Produto
from django.db.models import Q
from pprint import pprint

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def monte(request):

    if str(request.method).lower() == 'post':

        balca = request.POST.get('bolsa-alca')
        bfrente = request.POST.get('bolsa-frente')
        batras = request.POST.get('bolsa-atras')
        btransversal = request.POST.get('bolsa-transversal')
        
        if (
            (balca == None or str(balca).strip() == '') or
            (bfrente == None or str(bfrente).strip() == '') or
            (batras == None or str(batras).strip() == '') or
            (btransversal == None or str(btransversal).strip() == '')
        ):
            # Redireciona se não estiver de acordo
            return redirect(reverse('home:monte'))
        
        
        print(request.POST)
        return redirect(reverse('home:monte'))
        
        products_id = NuvemShopApi.get_products_id(products_urls=[
            'https://enepta.lojavirtualnuvem.com.br/produtos/carro-importado/',
            'https://enepta.lojavirtualnuvem.com.br/produtos/jaqueta-de-couro/'
        ])

        products_list_variants = []
        for prod_url, prod_id in products_id:
            products_list_variants.append({'variant_id': int(prod_id), 'quantity': 1})

        data = {
            'contact_name': 'teste',
            'contact_lastname': 'testedg',
            'contact_email': 'teste@gmail.com',
            'payment_status': 'unpaid',
            'products': products_list_variants,
        }
        cart = NuvemShopApi.post('/draft_orders/', data=data)

        checkout_url = cart['checkout_url']
        return redirect(to=checkout_url)

    else:
        produtos = Produto.objects.filter(Q(ativo=True))

        return render(request, 'home/monte.html', context={'produtos': produtos})
    


