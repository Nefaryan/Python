import random

numeri = []
for i in range(5):
    numeri.append(random.randint(0, 100))

contenuto_file = '\n'.join([str(numero) for numero in numeri])

with open("numeri.txt", "w") as file:
    file.write(contenuto_file)  

# Legge i numeri dal file
with open("numeri.txt", "r") as file:
    numeri_da_file = [int(line.strip()) for line in file.readlines()]

numeri_indovinati = []
count = 0

while count < 7:
    num = input("Ciao Utente, dammi un numero oppure scrivi 'esci' per terminare: ")
    if num.lower() == "esci":
        break
    try:
        num = int(num)
        if num in numeri_da_file and num not in numeri_indovinati:
            print("Hai indovinato il numero!")
            numeri_indovinati.append(num)
        elif num in numeri_indovinati:
            print("Hai già indovinato questo numero.")
        else:
            print("Numero sbagliato, riprova.")
        count += 1
        print(f"Tentativo numero {count}, ti rimangono ancora {7 - count} tentativi")
    except ValueError as e:
        print("Per favore inserisci un numero valido.", e)

print("\nGrazie per aver giocato!")

if len(numeri_indovinati) >= 2:
    print("Hai vinto! Complimenti, hai indovinato almeno due numeri.")
else:
    print("Hai perso. Non sei riuscito ad indovinare almeno due numeri.")

print("Numeri da indovinare:", numeri_da_file)
print("Numeri che hai indovinato:", numeri_indovinati)
