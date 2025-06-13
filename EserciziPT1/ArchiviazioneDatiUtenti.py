clienti = {}

while True:
    nome = input("Inserisci un nome, esci per uscire o prezzo per il prezzo: ")
    if nome.lower() == "esci": break

    elif nome.lower() != "prezzo":
        age = int(input("Quanti anni ha? "))
        exp = int(input("Quanti anni di esperienza alla guida ha? "))
        acc = int(input("Numero incidenti negli ultimi 5 anni? "))
        package = input("Opzione pacchetto?(Base, Intermedio, Premium) ")
        package.lower()

        info = {"età":age, "esperienza":exp, "incidenti":acc, "pacchetto":package}
        clienti[nome] = info

    else:
        for i in clienti:
            prezzobase = 500
            if clienti[i]["età"] <18:
                print("Non sei idoneo per l'assicurazione")
                continue
            elif clienti[i]["età"] >=18 and clienti[i]["età"] <= 25: prezzobase1 = prezzobase*(1+20/100)
            elif clienti[i]["età"] >=26 and clienti[i]["età"] <= 50: prezzobase1 = prezzobase
            elif clienti[i]["età"] > 50: prezzobase1 = prezzobase*0.9
            if clienti[i]["esperienza"] <2: prezzobase1 = prezzobase*(30/100) + prezzobase1
            if clienti[i]["incidenti"] ==1: prezzobase1 = prezzobase*(15/100) + prezzobase1
            elif clienti[i]["incidenti"] >=2 and clienti[i]["incidenti"]<=4: prezzobase1 = prezzobase*(30/100) + prezzobase1
            elif clienti[i]["incidenti"] >4: 
                print("Non sei idoneo per l'assicurazione")
                continue
            if clienti[i]["pacchetto"] == "intermedio": prezzobase1 = prezzobase*(20/100) + prezzobase1
            elif clienti[i]["pacchetto"] == "premium": prezzobase1 = prezzobase*(50/100) + prezzobase1
           # preventivi.append(prezzobase)
            clienti[i]["preventivo"] = prezzobase1
            print(f"Nome: {i} Prezzo: {prezzobase1}")
        break
    
print(clienti)

    
    
    