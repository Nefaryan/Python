def changeVoti():
    print("Sei nella modalità di Modifica di uno Studente!")

    with open("Studenti.txt", "r") as fileL:
        studenti = fileL.readlines()

    matricola_input = input("Inserire matricola dello studente da modificare: ")
    trovato = False

    for i in range(len(studenti)):
        riga = studenti[i].replace('\n', '')
        parti = riga.split()

        if parti[0] == matricola_input:
            trovato = True
            nome = parti[1]
            cognome = parti[2]
            # Estrai solo i voti numerici prima della parola "MEDIA:"
            voti_raw = parti[3:]
            voti = []
            for val in voti_raw:
                if val.startswith("MEDIA:"):
                    break
                if val != "-":
                    try:
                        voti.append(int(val))
                    except:
                        pass

            print(f"\nStudente trovato: {nome} {cognome}")
            print(f"Voti attuali: {voti}")

            azione = input("Vuoi aggiungere un voto (a) o eliminarne uno (e)? ").lower()

            if azione == "a":
                nuovo_voto = input("Inserisci il nuovo voto da aggiungere: ")
                if nuovo_voto.isdigit():
                    voti.append(int(nuovo_voto))
                    print("Voto aggiunto.")
                else:
                    print("Voto non valido.")
            elif azione == "e":
                voto_da_rimuovere = input("Quale voto vuoi eliminare?: ")
                if voto_da_rimuovere.isdigit():
                    voto_int = int(voto_da_rimuovere)
                    if voto_int in voti:
                        voti.remove(voto_int)
                        print("Voto eliminato.")
                    else:
                        print("Voto non trovato.")
                else:
                    print("Voto non valido.")

            # Ricalcola media
            media = round(sum(voti) / len(voti), 2) if voti else 0
            voti_str = " - ".join(str(v) for v in voti)

            nuova_riga = f"{matricola_input} {nome} {cognome} {voti_str} MEDIA: {media}\n"
            studenti[i] = nuova_riga
            break

    if not trovato:
        print("Matricola non trovata.")
    else:
        with open("Studenti.txt", "w") as fileL:
            fileL.writelines(studenti)
        print("Modifica completata.")