class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione

    def __repr__(self):
        return f"{self.nome} ({self.__class__.__name__}) - Prezzo: {self.prezzo_vendita}€"

#________________________________________________________________________________________________
#________________________________________________________________________________________________


class Elettronica(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia_anni):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.garanzia_anni = garanzia_anni

#________________________________________________________________________________________________
#________________________________________________________________________________________________

class Abbigliamento(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.materiale = materiale

#________________________________________________________________________________________________
#________________________________________________________________________________________________

class Fabbrica:
    def __init__(self, budget_iniziale):
        self.inventario = {} 
        self.profitto_totale = 0
        self.budget = budget_iniziale

    #Controlla se la quantità è positiva; se no, stampa errore e torna indietro.
    def aggiungi_prodotto(self, prodotto, quantita):
        if quantita <= 0:
            print("Quantità non valida.")
            return
        #Calcolo del costo totale della produzione
        costo_totale = prodotto.costo_produzione * quantita
        
        #Controllo se il budget è sufficiete è in caso non lo è stampa un errore
        if self.budget < costo_totale:
            print(f"Budget insufficiente. Servono {costo_totale:.2f}€, ma hai solo {self.budget:.2f}€.")
            return

        #Aggiornamento del budget
        self.budget -= costo_totale

        #Se il prodotto non è già presente nell'inventario , crea una lista vuota per quel prodotto
        if prodotto.nome not in self.inventario:
            self.inventario[prodotto.nome] = []

        #Aggiunge alla lista del prodotto tante copie dell'oggetto prodotto quanti sono specificati dalla quantità.
        for _ in range(quantita):
            self.inventario[prodotto.nome].append(prodotto)

        print(f"Aggiunti {quantita} pezzi di {prodotto.nome}. Spesa: {costo_totale:.2f}€. Nuovo budget: {self.budget:.2f}€")
    #________________________________________________________________________________________________
  
    def vendi_prodotto(self, nome, quantita):
        
        if nome not in self.inventario or len(self.inventario[nome]) < quantita:
            print("Prodotto non disponibile in quantità richiesta.")
            return

        venduti = [self.inventario[nome].pop() for _ in range(quantita)]
        prezzo_totale = venduti[0].prezzo_vendita * quantita
        profitto_unitario = venduti[0].calcola_profitto()

        self.profitto_totale += profitto_unitario * quantita
        self.budget += prezzo_totale

        print(f"Vendute {quantita} unità di {nome}. Ricavo: {prezzo_totale:.2f}€. Budget attuale: {self.budget:.2f}€")
    #________________________________________________________________________________________________
   
    def resi_prodotto(self, prodotto, quantita):
      
        if quantita <= 0:
            print("Quantità non valida.")
            return
        
        #Se il prodotto non è ancora nell'inventario, crea la lista vuota per quel prodotto
        if prodotto.nome not in self.inventario:
            self.inventario[prodotto.nome] = []

        #Aggiunge nuovamente il prodotto restituito all'inventario
        for _ in range(quantita):
            self.inventario[prodotto.nome].append(prodotto)

        prezzo_totale = prodotto.prezzo_vendita * quantita
        profitto_unitario = prodotto.calcola_profitto()

        self.profitto_totale -= profitto_unitario * quantita
        self.budget -= prezzo_totale

        print(f"Reso di {quantita} unità di '{prodotto.nome}'. Rimborso cliente: -{prezzo_totale:.2f}€. Budget attuale: {self.budget:.2f}€")
    #________________________________________________________________________________________________
    def stampa_inventario(self):
        print("\nInventario attuale:")
        if not self.inventario:
            print("  (vuoto)")
            return

        for nome, lista in self.inventario.items():
            if lista:
                print(f"- {nome} ({lista[0].__class__.__name__}) | Quantità: {len(lista)}")

    def stampa_profitto_totale(self):
        print(f"Profitto totale: {self.profitto_totale:.2f}€")

    def mostra_budget(self):
        print(f"Budget attuale: {self.budget:.2f}€")


#________________________________________________________________________________________________
#________________________________________________________________________________________________
#________________________________________________________________________________________________
#________________________________________________________________________________________________


def richiedi_budget():
    while True:
        try:
            budget = float(input("Inserisci il budget iniziale della fabbrica (€): "))
            if budget <= 0:
                print(" Inserisci un importo positivo.")
            else:
                return budget
        except ValueError:
            print("Inserisci un numero valido.")

def menu_fabbrica():
    try:
        budget = float(input("Inserisci il budget iniziale (€): "))
    except ValueError:
        print("Valore non valido. Uscita.")
        return

    fabbrica = Fabbrica(budget)

    while True:
        print("\n===== MENU FABBRICA =====")
        print("1. Aggiungi prodotto")
        print("2. Vendi prodotto")
        print("3. Reso prodotto")
        print("4. Mostra inventario")
        print("5. Mostra budget e profitto")
        print("0. Esci")

        scelta = input("Scelta: ").strip()

        if scelta == "1":
            nome = input("Nome prodotto: ").strip()
            tipo = input("Tipo (elettronica/abbigliamento): ").strip().lower()

            try:
                costo = float(input("Costo produzione: "))
                prezzo = float(input("Prezzo vendita: "))
                quantita = int(input("Quantità: "))
                if costo < 0 or prezzo < 0 or quantita <= 0:
                    raise ValueError
            except ValueError:
                print("Valori numerici non validi.")
                continue

            if tipo == "elettronica":
                garanzia = input("Garanzia (anni): ").strip()
                prodotto = Elettronica(nome, costo, prezzo, garanzia)
            elif tipo == "abbigliamento":
                materiale = input("Materiale: ").strip()
                prodotto = Abbigliamento(nome, costo, prezzo, materiale)
            else:
                print("Tipo prodotto non valido.")
                continue

            fabbrica.aggiungi_prodotto(prodotto, quantita)

        elif scelta == "2":
            nome = input("Nome prodotto da vendere: ").strip()
            try:
                quantita = int(input("Quantità: "))
                if quantita <= 0:
                    raise ValueError
            except ValueError:
                print("Quantità non valida.")
                continue

            fabbrica.vendi_prodotto(nome, quantita)

        elif scelta == "3":
            nome = input("Nome prodotto da restituire: ").strip()
            try:
                quantita = int(input("Quantità: "))
                if quantita <= 0:
                    raise ValueError
            except ValueError:
                print("Quantità non valida.")
                continue

            if nome in fabbrica.inventario and fabbrica.inventario[nome]:
                prodotto_esistente = fabbrica.inventario[nome][0]
                fabbrica.resi_prodotto(prodotto_esistente, quantita)
            else:
                print("Prodotto non trovato in inventario.")

        elif scelta == "4":
            fabbrica.stampa_inventario()

        elif scelta == "5":
            fabbrica.mostra_budget()
            fabbrica.stampa_profitto_totale()

        elif scelta == "0":
            print("Chiusura programma.")
            break

        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    menu_fabbrica()
