print("Inserisci le parole")
print("Scrivi 'esci' per uscire e vedere la lunghezza delle parole inserite")

parole = []

while True :
    p = input()
    p = p.replace(" ","")
    if p.lower() == "esci":
        break
    parole.append(p)

print ("\nLunghezza parole inserite")
for w in parole : 
       print(f"La parola '{w}' ha {len(w)} caratteri.") 

