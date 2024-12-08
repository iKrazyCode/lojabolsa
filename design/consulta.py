import requests

# Dados do usuário
user_id = "5302321"
access_token = "41cb849eaf9c3a5f5a5edd2ca1ae4e52202e922d"

# Endpoint
url = f"https://api.tiendanube.com/v1/{user_id}/products/"

# Headers
headers = {
    "Authentication": f"bearer {access_token}",
    "Content-Type": "application/json",
    "User-Agent": "teste (meuemail@dominio.com)"
}

produto_url = "https://enepta.lojavirtualnuvem.com.br/produtos/carro-importado/"
produto_handle = produto_url.split('/')[-1] if not produto_url.endswith('/') else produto_url.split('/')[-2]


r = requests.get(url, headers=headers, params={'handle': produto_handle})

print(r.content)