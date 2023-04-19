import os
import requests
from dotenv import load_dotenv

os.system('cls')

load_dotenv()

def get_oauth():
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    username = os.getenv('USER_ACCOUNT')
    password = os.getenv('PASSWORD_ACCOUNT')

    url = 'https://api.netatmo.com/oauth2/token'
    params = {
        'grant_type': 'password',
        'client_id': f'{client_id}',
        'client_secret': f'{client_secret}',
        'username': f'{username}',
        'password': f'{password}',
        'scope': 'read_station'
    }

    response = requests.post(url, data=params, timeout=10)
    if response.ok:
        token = response.json()['access_token']
        # print(f'Token récupéré : {token}')
        return token
    # else:
        # print(f'Erreur lors de la récupération du token : {response.status_code}')
