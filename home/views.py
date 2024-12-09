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
        contact_name = request.POST.get('contact-name')
        contact_lastname = request.POST.get('contact-lastname')
        contact_email = request.POST.get('contact-email')
        
        if (
            (balca == None or str(balca).strip() == '') or
            (bfrente == None or str(bfrente).strip() == '') or
            (batras == None or str(batras).strip() == '') or
            (btransversal == None or str(btransversal).strip() == '')
        ):
            # Redireciona se não estiver de acordo
            return redirect(reverse('home:monte'))
        

        products_ids = NuvemShopApi.get_products_id(products_urls=[
            balca,
            bfrente,
            batras,
            # btransversal[0]
        ])

        products_list_variants = []
        for prod_url, prod_id in products_ids:
            products_list_variants.append({'variant_id': int(prod_id), 'quantity': 1})

        data = {
            'contact_name': f"{contact_name}",
            'contact_lastname': f"{contact_lastname}",
            'contact_email': f"{contact_email}",
            'payment_status': 'unpaid',
            'products': products_list_variants,
        }
        cart = NuvemShopApi.post('/draft_orders/', data=data)

        checkout_url = cart['checkout_url']
        return redirect(to=checkout_url)

    else:
        produtos = Produto.objects.filter(Q(ativo=True))

        return render(request, 'home/monte.html', context={'produtos': produtos})
    


