print("Calcolatrice")
print("Inserisci un numero, poi un'operazione (+, -, *, /), poi un altro numero.")
print("Scrivi '=' per ottenere il risultato, o 'Esci' per uscire.")

totale = None
operazione = None

while True:
    ingresso = input()

    if ingresso == "Esci":
        print("Uscita dal programma.")
        break

    if ingresso == "=":
        print("Risultato:", totale) if totale is not None else print("Nessun calcolo da eseguire.")
        totale, operazione = None, None
        continue

    if ingresso in ["+", "-", "*", "/"]:
        if totale is None:
            print("Errore inserisci prima un numero.")
            continue
        operazione = ingresso
        continue

    numero = float(ingresso)  

    if totale is None:
        totale = numero
        continue

    if operazione is None:
        print("Errore nell'input.")
        continue

    totale = (
    totale + numero if operazione == "+" else
    totale - numero if operazione == "-" else
    totale * numero if operazione == "*" else
    totale / numero if operazione == "/" and numero != 0 else
    None)


    if operazione == "/" and numero == 0:
        print("Errore non puoi dividere per zero!")

    operazione = None
