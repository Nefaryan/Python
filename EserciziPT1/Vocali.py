vocali = "aeiouAEIOU";

testo = input("Inserisci una parola o una frase: ")
i = 0;
for c in testo:
    if c in vocali:
     print(f"Vocale '{c}' trovata all'indice {i}")
    i+=1
