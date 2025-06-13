num1 = float(input("Inserisci il primo numero: "))
num2 = float(input("Inserisci il secondo numero: "))
operazione = input("Scegli un'operazione (+, -, *, /): ")

if operazione == "+":
    risultato = num1 + num2
elif operazione == "-":
    risultato = num1 - num2
elif operazione == "*":
    risultato = num1 * num2
elif operazione == "/":
    risultato = num1 / num2 if num2 != 0 else "Errore: divisione per zero!"
else:
    risultato = "Operazione non valida."

print(f"Risultato : {risultato}")