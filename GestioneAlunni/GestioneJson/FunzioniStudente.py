def aggiungi_studente(dati):
    nome = input("Nome: ")
    cognome = input("Cognome: ")
    voti = []
    
    while True:
        voto = input("Inserisci voto (oppure 'fine'): ")
        if voto.lower() == "fine":
            break
        try:
            voti.append(int(voto))
        except ValueError:
            print("Inserisci un numero valido")

    media = round(sum(voti)/len(voti), 2) if voti else 0

    nuovo_Studente = {
            "id": dati["last_id"] + 1,
            "nome": nome,
            "cognome": cognome,
            "voti": voti,
            "media": media
        }

    dati["students"].append(nuovo_Studente)
    dati["last_id"] = nuovo_Studente["id"]
    print("Studente aggiunto.")

def mostra_studenti(dati):
    for studente in dati["students"]:
        print(f"{studente['id']} - {studente['nome']} {studente['cognome']} | Voti: {studente['voti']} | Media: {studente['media']}")

def modifica_voti(dati):
    id_input = input("ID dello studente da modificare: ")
    for studente in dati["students"]:
        if str(studente["id"]) == id_input:
            print("Voti attuali:", studente["voti"])
            scelta = input("Vuoi (a)ggiungere o (r)imuovere un voto? ").lower()

            if scelta == "a":
                voto = int(input("Voto da aggiungere: "))
                studente["voti"].append(voto)
            elif scelta == "r":
                voto = int(input("Voto da rimuovere: "))
                if voto in studente["voti"]:
                    studente["voti"].remove(voto)
                else:
                    print("Voto non trovato.")
            else:
                print("Scelta non valida.")

            # aggiorna media
            voti = studente["voti"]
            studente["media"] = round(sum(voti)/len(voti), 2) if voti else 0
            print("Voti aggiornati.")
            return
    print("Studente non trovato.")
    

def elimina_studente(dati):
    id_input = input("ID dello studente da eliminare: ")
    for i, studente in enumerate(dati["students"]):
        if str(studente["id"]) == id_input:
            print("Eliminato:", studente["nome"], studente["cognome"])
            dati["students"].pop(i)
            return
    print("Studente non trovato.")

                   