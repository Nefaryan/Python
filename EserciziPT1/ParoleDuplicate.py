def parole_duplicate(testo):
    
    punteggiatura = ".,;!?\"'()" 
    testo = testo.lower()  

    testo = "".join([char for char in testo if char not in punteggiatura])

    parole = testo.split()

    duplicati = {}
    
    flag = False

    for parola in parole:
        if parola not in duplicati:
            duplicati[parola] = 1
        else:
            duplicati[parola] += 1

    for parola, occorrenze in duplicati.items():
        if occorrenze > 1:
            flag = True
            print(f"'{parola}' è un duplicato, appare {occorrenze} volte ed è lunga {len(parola)} caratteri.")
    
    if not flag:
        print("Non ci sono duplicati")

frase = input("Inserisci la frase da controllare: ")
parole_duplicate(frase)