"""Function to requests the weather API from Netatmo, writing CSV files."""
import os
# import time
import datetime
import requests
# Pour importer le fichier get_oauth.py
import get_oauth as getOauth

os.system('cls')

def fetch_data():
    """
    Retrieving data from the Netatmo API
    """

    url = 'https://api.netatmo.com/api/getpublicdata'
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {getOauth.get_oauth()}'
    }
    params = {
        'lat_ne': '49.840694',
        'lon_ne': '4.766453',
        'lat_sw': '49.834181',
        'lon_sw': '4.757583',
        'required_data': 'temperature',
        'filter': 'false'
    }
    response = requests.get(url, headers=headers, params=params, timeout=10)
    if response.ok:
        return response.json()
    else:
        print('Impossible de contacter le serveur')
        return False
    # raise Exception('Impossible de contacter le serveur')
# Fin

def write_file():
    """
    Writing data to a CSV file
    """
    data = fetch_data()

    if data:
        src_input = "data/input/"
        # Date complete
        date_heure = datetime.datetime.now()
        new_date = date_heure.strftime("%Y-%m-%d %H:%M:00")
        currently_date = date_heure.strftime("%Y-%m-%d")
        print(f"Data write at {new_date}")

        measures = data['body'][0]["measures"]["02:00:00:7f:bf:5c"]
        first_key = list(measures['res'].keys())[0]
        temp = measures['res'][first_key][0]

        with open(f"{src_input}temp-{currently_date}.csv", 'a',encoding='utf-8') as f:
            f.write(f"{new_date},{temp}\n")
    else:
        print("Data not received")
# Fin
