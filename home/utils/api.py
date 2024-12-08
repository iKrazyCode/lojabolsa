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
        r.raise_for_status()
        return r.json()


    @staticmethod
    def post(endpoint: str, data:dict=None):
        endpoint = endpoint if not endpoint.startswith('/') else endpoint[1:]
        r = requests.post(
            f"{NuvemShopApi.BASE_URL}{endpoint}",
            headers=NuvemShopApi.HEADERS,
            json=data)
        r.raise_for_status()
        return r.json()
     