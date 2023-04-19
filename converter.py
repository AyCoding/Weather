"""Converter from CSV to JSON"""
import os
import datetime
import pandas as pd

os.system('cls')

def converterCSVtoJSON():
    """Converter from CSV to JSON"""
    date_heure = datetime.datetime.now()
    currently_date = date_heure.strftime("%Y-%m-%d")

    src = f"data/input/temp-{currently_date}.csv"
    src_output = "data/output/"

    # Lecture des fichiers dans un DataFrame
    df = pd.read_csv(src, header=None, names=['date', 'temp'])

    # Conversion du CSV en JSON
    data_set = df.to_json(orient='records') # orient='index' / orient='columns' (default)

    # Ecriture des fichiers avec les données converti en JSON dans /data/output/...csv
    with open(f"{src_output}temp-{currently_date}.json", 'w', encoding='utf-8') as file_json:
    # with open(f"{src_output}temp-{currently_date}.json", 'w', encoding='utf-8') as file_json:
        file_json.write(data_set)
        print('Convert successful')
converterCSVtoJSON()