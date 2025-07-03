import requests


def ricerca_città(nome:str):
    try:
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={nome}&count=1&language=it&format=json"
        response = requests.get(url)
        print("Sto cercando le coordinate...")
        dictResponse = response.json()
        print("Coordinate trovate!\n")
        if not dictResponse.get("results"):
           print(f"Città '{nome}' non trovata.")
        return dictResponse["results"][0]["longitude"], dictResponse["results"][0]["latitude"]
    except requests.RequestException as e:
        print("Errore nella richiesta alla Geocoding API:", e)
        return None,None
    except Exception as e:
        print(e)
        return None,None

def previsioni(lon:float, lat:float, n_giorni:int, v_vento, prec):
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m"
        if prec:
            url += ",precipitation_probability"
        if v_vento:
            url += ",wind_speed_10m"

        if n_giorni == "1": url += "&forecast_days=1"
        elif n_giorni == "3": url += "&forecast_days=3"

        print("Ricerca previsioni...")
        response = requests.get(url)
        dictResponse = response.json()
        print("Ricerca completata!\n")

        return dictResponse["hourly"]
    except requests.RequestException as e:
        print("Errore nella richiesta alla Geocoding API:", e)
        return None
    except Exception as e:
        print(e)
        return None
        
        

def stampa_previsioni_meteo(dati, mostra_vento, mostra_precipitazioni):
    if dati == None:
        print("Errore! Dati nonpresenti.")
        exit()
    orari = dati["time"]
    temperature = dati["temperature_2m"]
    precipitazioni = dati.get("precipitation_probability", [])
    vento = dati.get("wind_speed_10m", [])

    print("\n---PREVISIONI METEO---")

    previsioni_per_giorno = {}

    for i in range(len(orari)):
        orario = orari[i]
        giorno, ora = orario.split("T")

        riga = f"Orario: {ora} - Temperatura: {temperature[i]}°C"

        if mostra_precipitazioni and precipitazioni:
            riga += f" | Prob. Precipitazioni: {precipitazioni[i]}%"

        if mostra_vento and vento:
            riga += f" | Vento: {vento[i]} km/h"

        if giorno not in previsioni_per_giorno:
            previsioni_per_giorno[giorno] = []
        previsioni_per_giorno[giorno].append(riga)

    for giorno, righe in previsioni_per_giorno.items():
        print(f"\nData: {giorno}")
        for riga in righe:
            print(riga)


while True:
    cit = input("Di che città vuoi vedere il meteo?: ").replace(" ","+").lower()
    days = input("Per quanti giorni vuoi vedere le previsioni? (1,3,7): ")
    v = input("Vuoi vedere anche il vento? (1 per sì, 0 per no): ")
    p = input("Vuoi vedere anche le precipitazioni? (1 per sì, 0 per no): ")

    if days not in ["1","3","7"]:
        print("Errore d'inserimento!")
        continue
    
    if v == "1": v = True
    elif v == "0": v = False
    else:
        print("Errore d'inserimento!")
        continue

    if p == "1": p = True
    elif p == "0": p = False
    else:
        print("Errore d'inserimento!")
        continue

    lon,lat = ricerca_città(cit)
    forecast = previsioni(lon, lat, days, v, p)
    stampa_previsioni_meteo(forecast, v, p)
    print("\n")
    
    out = input("Vuoi uscire? -1 per uscire: ")
    if out == "-1": break

print("Fine Programma. Grazie per l'uso. 🔥 ")