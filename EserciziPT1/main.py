nome = input("Inserisci il tuo nome: ")
#cognome = input("Inserisci il tuo cognome: ")
#mail = input ("Inserisci la tua mail :")
anno_nascita = int(input("Inserisci il tuo anno di nascita: "))
giorno_settimana = int(input("Inserisci il giorno della settimana attuale (1 = Lunedì, 7 = Domenica): "))

anno_corrente = 2025
eta = anno_corrente - anno_nascita

giorni_mancanti = (6 - giorno_settimana) % 7

print(f"Il tuo nome è {nome}\nhai {eta} anni\ne mancano {giorni_mancanti} giorni a sabato")
