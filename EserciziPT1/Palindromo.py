def isPalindromo(testo):
    testo = testo.lower()
    validChar = ""
    for char in testo:
        if char.isalnum():
            validChar += char
    
    return validChar == validChar[::-1]

frase = input("Inserisci la frase: ")

if isPalindromo(frase):
    print("La Stringa è palindroma")
else:
    print ("La Stringa non è palindroma")