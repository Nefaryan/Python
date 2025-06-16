def addStudent(matricola):
    print("Modalità: Aggiunta Studente")
    studenti = []

    while True:
        nome = input("Nome dello studente (oppure 'fine' per uscire): ")
        if nome.lower() == "fine":
            break
        cognome = input("Cognome dello studente: ")
        voti = []
        while True:
            voto = input("Inserisci un voto (oppure 'fine' per terminare i voti): ")
            if voto.lower() == "fine":
                break
            if voto.isdigit():
                voti.append(int(voto))
            else:
                print("Inserisci un numero valido.")

        if voti:
            media = round(sum(voti) / len(voti), 2)
        else:
            media = 0

        matricola += 1
        voti_str = " - ".join(str(v) for v in voti)
        riga = f"{matricola} {nome} {cognome} {voti_str} MEDIA: {media}\n"
        studenti.append(riga)

    with open("Studenti.txt", "a") as fileS:
        for studente in studenti:
            fileS.write(studente)

    print("Studenti aggiunti correttamente.")
    return matricola