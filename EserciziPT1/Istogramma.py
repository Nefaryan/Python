numeri_input = input("Inserisci una lista di numeri separati da spazi: ")
tokens = numeri_input.split()

numeri = []
for t in tokens:
    if t.isdigit():
        numeri.append(int(t))
    else:
        print(f"Attenzione: '{t}' non è un numero e verrà ignorato.")

print("\nIstogramma:")
for n in numeri:
    id = str('*' * n)
    print(id, (id[::-1]))

