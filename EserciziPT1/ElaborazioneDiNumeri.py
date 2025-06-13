n = int(input("Inserisci un numero:" ))

quadrato = n**2

pari = "pari" if n % 2 == 0 else "dispari"

cifre = len(str(n))

dizionario = {
    'quadrato': quadrato,
    'pari o dispari': pari,
    'n. cifre': cifre
}

print(f"Numero inserito {n}, {dizionario}")