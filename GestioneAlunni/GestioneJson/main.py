import time
import json
import FunzioniStudente as f

percorsojson = "GestioneAlunni\GestioneJson\Studenti.json"

def leggi_json():
    try:
        with open(percorsojson, "r",encoding="utf-8")as file:
         return json.load(file)
    except FileNotFoundError:
        return []
          
    
def scrivi_json(studenti):
    try:
        with open(percorsojson, "w", encoding="utf-8")as file:
            json.dump(studenti,file, indent=4)
    except:
        pass
        
studenti = leggi_json()

while True:
    print("\n--- GESTIONE STUDENTI ---")
    print("1. Aggiungi studente")
    print("2. Modifica voti")
    print("3. Elimina studente")
    print("4. Visualizza tutti")
    print("5. Salva ed esci")
    scelta = input("Scelta: ")

    if scelta == "1":
        f.aggiungi_studente(studenti)
    elif scelta == "2":
        f.modifica_voti(studenti)
    elif scelta == "3":
        f.elimina_studente(studenti)
    elif scelta == "4":
        f.mostra_studenti(studenti)
    elif scelta == "5":
        scrivi_json(studenti)
        print("Dati salvati. Arrivederci!")
        break
    else:
        print("Scelta non valida.")
    time.sleep(1)


