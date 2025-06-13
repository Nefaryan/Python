n1 = int(input("Inserisci il primo numero: "))
n2 = int(input("Inserisci il secondo numero: "))
n3 = int(input("Inserisci il terzo numero: "))

if n1 == n2 and n2 == n3 : print("I tre numeri sono uguali")
elif n1 == n2 or n2 == n3 or n1 == n3 :print("Ci sono 2 numeri uguali")
else:
    max = n2 if n2 > n1 else n1
    max = n3 if n3 > max else max
print(f"il Numero più grande è {max}")