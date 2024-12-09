from django.conf import settings
import requests


class NuvemShopApi:
    """
    API para usar na nuvem shop
    """
    BASE_URL = settings.NUVEMSHOP_BASE_URL
    HEADERS = {
        "Authentication": f"bearer {settings.NUVEMSHOP_ACCESS_TOKEN}",
        "User-Agent": "Site (teste@gmail.com)"
    }

    @staticmethod
    def get(endpoint: str, params=None):
        endpoint = endpoint if not endpoint.startswith('/') else endpoint[1:]
        r = requests.get(
            f"{NuvemShopApi.BASE_URL}{endpoint}",
            headers=NuvemShopApi.HEADERS,
            params=params
            )
        
        r.raise_for_status() if settings.DEBUG == False else None
        return r.json()


    @staticmethod
    def post(endpoint: str, data:dict=None):
        endpoint = endpoint if not endpoint.startswith('/') else endpoint[1:]
        r = requests.post(
            f"{NuvemShopApi.BASE_URL}{endpoint}",
            headers=NuvemShopApi.HEADERS,
            json=data)
        
        
        r.raise_for_status() if settings.DEBUG == False else None
        return r.json()

    # Helpers
    @staticmethod
    def get_products_id(products_urls=list) -> list:
        """
        Retorna uma lista com o [URL do produto, id do produto] de cada produto contido em products_url
        """
        list_id = []
        for url in products_urls:
            url_part = str(url)
            if str(url_part).endswith('/'):
                url_part = url_part[:-1].split('/')[-1]
            else:
                url_part = url_part.split('/')[-1]
            
            r = NuvemShopApi.get('/products/', params={'handle': url_part, 'fields': 'variants'})
            prod_id = r
            print(url, prod_id)
            list_id.append([url, str(prod_id[0]['variants'][0]['id'])])

        return list_id
    




