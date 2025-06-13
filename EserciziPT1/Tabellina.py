
while True:
    n = input("Inserisci un numero: ")
    if n.isdigit():
        print("valore valido")
        break
    else :
        print("valore non valido inseriscine un altro")

print(f"Tabellina del {n}:")
i = 1
while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1

for num in range(11):
   print(f"{n} x {num} = {n * num}") 