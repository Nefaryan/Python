
eta = int(input("Quanti anni hai? "))
patente = input("Hai la patente? (si/no): ")
bevuto = input("Hai bevuto? (si/no): ")

if eta >= 18 and patente == "si" and bevuto == "no": print("Puoi guidare.")
else:print("Non puoi guidare.")

if eta < 18 : print("sei minorenne no puoi guidare")
elif patente == "no": print("non puoi guidare.")
elif bevuto == "si" : print("hai bevuto non puoi guidare")
else:print("Puoi guidare.") 
