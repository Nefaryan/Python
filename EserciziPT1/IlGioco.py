print("Indovina il numero")

while True:
    numero_input = input("Giocatore 1, inserisci un numero da 1 a 100: ")
    if numero_input.isdigit():
        numero_segreto = int(numero_input)
        if 1 <= numero_segreto <= 100:
            break
        else:
            print("Il numero deve essere compreso tra 1 e 100.")
    else:
        print("Input non valido. Inserisci un numero intero tra 1 e 100.")

print("--- È il turno del Giocatore 2! Hai 5 tentativi per indovinare. ---")

tentativi_totali = 5
tentativi_usati = 0

while True:
    tentativi_rimasti = tentativi_totali - tentativi_usati

    if tentativi_rimasti == 0:
        print(f"Hai esaurito i tentativi. Il numero era: {numero_segreto}")
        break

    risposta = input(f"Tentativo {tentativi_usati + 1}/5 (rimangono {tentativi_rimasti}): inserisci un numero o 'mi arrendo': ")

    if risposta == "mi arrendo":
        print(f"Hai rinunciato. Il numero era: {numero_segreto}")
        break

    if not risposta.isdigit():
        print("Input non valido. Inserisci un numero o 'mi arrendo'.")
        continue

    numero = int(risposta)

    if numero < 1 or numero > 100:
        print("Il numero deve essere tra 1 e 100.")
        continue

    tentativi_usati += 1

    if numero == numero_segreto:
        print(f"Complimenti! Hai indovinato il numero! Il numero era {numero_segreto}")
        break
    elif numero < numero_segreto:
        print("Numero troppo basso.")
    else:
        print("Numero troppo alto.")
