def cifrario(testo, chiave, modalità):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    risultato = ""
    
    for char in testo.lower():
        if char in alfabeto:
            
            #minuscola = char.lower()
            #indice_orginale = alfabeto.index(minuscola)
            
            indice_orginale = alfabeto.index(char)
            
            if modalità == "cript":
                nuovo_indice = (indice_orginale + chiave) % 26
            elif modalità == "decript":
                nuovo_indice = (indice_orginale - chiave) % 26
            nuovo_char = alfabeto[nuovo_indice]
            
            """
            if char.isupper():
                risultato += nuovo_char.upper()
            else:
                risultato += nuovo_char
            """
            risultato += nuovo_char
        else:
            risultato += char
    
    return risultato
    
            


testo = input("Testo da criptare o decriptare: ")
modalità = input("Scrivi 'cript' o decript per criptare o decriptare il testo: ").lower()
chiave = int(input("Inserisci il un mumero per la chiave: "))

r = cifrario(testo,chiave,modalità)

print(r)