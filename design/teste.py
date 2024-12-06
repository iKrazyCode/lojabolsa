import requests

# Dados do usuário
user_id = "5302321"
access_token = "41cb849eaf9c3a5f5a5edd2ca1ae4e52202e922d"

# Endpoint
url = f"https://api.tiendanube.com/v1/{user_id}/draft_orders"

# Headers
headers = {
    "Authentication": f"bearer {access_token}",
    "Content-Type": "application/json",
    "User-Agent": "teste (meuemail@dominio.com)"
}




corpo = {
    "contact_name": "Elon",
    "contact_lastname": "Musk",
    "contact_email": "teste@gmail.com",
    "payment_status": "unpaid",

    "products": [
        {
            "variant_id": 1080170975,
            "quantity": 99,
        }
    ],


}



# Fazer a requisição
response = requests.post(url, json=corpo, headers=headers)

# Verificar resposta
if response.status_code == 201:
    print("Draft Order criado com sucesso!")
    print(response.json())
else:
    print("Erro ao criar Draft Order:", response.status_code)
    print(response.json())
