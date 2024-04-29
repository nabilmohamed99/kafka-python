import json
import time
import urllib.request

from kafka import KafkaProducer

API_KEY = "241212b4a1b944aa9cf1e7a012589aaa39ff79a2"
url = "https://api.jcdecaux.com/vls/v1/stations?apiKey={}".format(API_KEY)

bootstrap_servers = "192.168.1.128:9092"

# Essayez de créer le producteur Kafka
try:
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
except Exception as e:
    print(f"Erreur lors de la création du producteur Kafka : {e}")
    exit(1)

# Boucle d'envoi des données au topic "velib-stations"
while True:
    try:
        # Récupérez les données à partir de l'API
        response = urllib.request.urlopen(url)
        stations = json.loads(response.read().decode())

        # Envoyez chaque station au topic Kafka
        for station in stations:
            producer.send("velib-stations", json.dumps(station).encode())

        # Affichez le nombre de stations envoyées
        print(f"{time.time()} Produit {len(stations)} enregistrements de station")

        # Attendez pendant une seconde
        time.sleep(1)

    except Exception as e:
        print(f"Erreur lors de l'envoi des données au topic Kafka : {e}")
