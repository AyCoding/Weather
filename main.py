import os
import time
# Pour importer le fichier weather.py
import weather as ws

# Pour importer le fichier converter.py
import converter as cv

os.system('cls')

# # Variable de vérification de la connexion à l'API
# Connexion = ws.fetch_data()
# # while True
# if Connexion:
#     print("Data receive")
#     now = time.localtime()
#     while True:
#         # Récupère l'heure actuelle
#         now = time.localtime()

#         if now.tm_min == 0 and now.tm_sec == 0:
#             ws.fetch_data()
#             ws.write_file()
#             cv.converterCSVtoJSON()

#         elif now.tm_min % 10 == 0 and now.tm_sec == 0:
#             ws.fetch_data()
#             ws.write_file()
#             cv.converterCSVtoJSON()
#         # Attend une seconde avant de vérifier à nouveau l'heure
#         time.sleep(1)
#     # Fin
# else:
#     print("Data not received")

while True:
    Connexion = ws.fetch_data()
    if Connexion:
        print("Data received")
        now = time.localtime()
        while True:
            # Récupère l'heure actuelle
            now = time.localtime()
            if now.tm_min == 0 and now.tm_sec == 0:
                ws.fetch_data()
                ws.write_file()
                cv.converterCSVtoJSON()

            elif now.tm_min % 10 == 0 and now.tm_sec == 0:
                ws.fetch_data()
                ws.write_file()
                cv.converterCSVtoJSON()

            # Attend une seconde avant de vérifier à nouveau l'heure
            time.sleep(1)
    else:
        print("Data not received. Retrying in 10 seconds...")
        time.sleep(10)
