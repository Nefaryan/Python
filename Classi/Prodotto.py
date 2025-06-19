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
<<<<<<< HEAD
        self.inventario = {} 
        self.profitto_totale = 0
        self.budget = budget_iniziale

    #Controlla se la quantità è positiva; se no, stampa errore e torna indietro.
=======
        self.inventario = {}
        self.profitto_totale = 0
        self.budget = budget_iniziale

>>>>>>> bba2dae5e5d0ec98b40464dc41b3c057c379535b
    def aggiungi_prodotto(self, prodotto, quantita):
        if quantita <= 0:
            print("Quantità non valida.")
            return
<<<<<<< HEAD
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

=======

        costo_totale = prodotto.costo_produzione * quantita
        if self.budget < costo_totale:
            print(f" Budget insufficiente. Servono {costo_totale:.2f}€, ma hai solo {self.budget:.2f}€.")
            return

        self.budget -= costo_totale

        if prodotto.nome in self.inventario:
            self.inventario[prodotto.nome]["quantita"] += quantita
        else:
            self.inventario[prodotto.nome] = {"prodotto": prodotto, "quantita": quantita}
        print(f" Aggiunti {quantita} pezzi di {prodotto.nome}. Spesa: {costo_totale:.2f}€. Nuovo budget: {self.budget:.2f}€")

    def vendi_prodotto(self, nome, quantita):
        if quantita <= 0:
            print(" Quantità non valida.")
            return

        if nome not in self.inventario:
            print(" Prodotto non trovato.")
            return
        if self.inventario[nome]["quantita"] < quantita:
            print(" Quantità insufficiente in magazzino.")
            return

        self.inventario[nome]["quantita"] -= quantita
        prodotto = self.inventario[nome]["prodotto"]
        profitto_unitario = prodotto.calcola_profitto()
        prezzo_totale = prodotto.prezzo_vendita * quantita
        self.profitto_totale += profitto_unitario * quantita
        self.budget += prezzo_totale
        print(f" Vendute {quantita} unità di {nome}. Ricavo: {prezzo_totale:.2f}€. Budget attuale: {self.budget:.2f}€")

    def resi_prodotto(self, nome, quantita):
        if quantita <= 0:
            print(" Quantità non valida.")
            return
        if nome in self.inventario:
            prodotto = self.inventario[nome]["prodotto"]
            prezzo_totale = prodotto.prezzo_vendita * quantita
            profitto_unitario = prodotto.calcola_profitto()

            if self.inventario[nome]["quantita"] + quantita < 0:
                print(" Reso non possibile: dati incoerenti.")
                return

            self.inventario[nome]["quantita"] += quantita
            self.profitto_totale -= profitto_unitario * quantita
            self.budget -= prezzo_totale
            print(f"Reso di {quantita} unità di '{nome}'. Rimborso cliente: -{prezzo_totale:.2f}€. Budget attuale: {self.budget:.2f}€")
        else:
            print(f" Il prodotto '{nome}' non è presente in inventario.")

    def stampa_inventario(self):
        print("\n Inventario attuale:")
        if not self.inventario:
            print("   (vuoto)")
            return
        for info in self.inventario.values():
            p = info["prodotto"]
            q = info["quantita"]
            print(f"- {p} | Quantità: {q}")

    def stampa_profitto_totale(self):
        print(f"\n Profitto totale: {self.profitto_totale:.2f}€")

    def mostra_budget(self):
        print(f" Budget attuale: {self.budget:.2f}€")
>>>>>>> bba2dae5e5d0ec98b40464dc41b3c057c379535b

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
<<<<<<< HEAD
    try:
        budget = float(input("Inserisci il budget iniziale (€): "))
    except ValueError:
        print("Valore non valido. Uscita.")
        return

    fabbrica = Fabbrica(budget)
=======
    budget_iniziale = richiedi_budget()
    fabbrica = Fabbrica(budget_iniziale)
>>>>>>> bba2dae5e5d0ec98b40464dc41b3c057c379535b

    while True:
        print("\n===== MENU FABBRICA =====")
        print("1. Aggiungi prodotto")
        print("2. Vendi prodotto")
<<<<<<< HEAD
        print("3. Reso prodotto")
        print("4. Mostra inventario")
        print("5. Mostra budget e profitto")
        print("0. Esci")

        scelta = input("Scelta: ").strip()
=======
        print("3. Mostra inventario")
        print("4. Reso di un prodotto")
        print("5. Mostra budget e profitto")
        print("0. Esci")
        scelta = input("Scelta: ")
>>>>>>> bba2dae5e5d0ec98b40464dc41b3c057c379535b

        if scelta == "1":
            nome = input("Nome prodotto: ").strip()
            tipo = input("Tipo (elettronica/abbigliamento): ").strip().lower()

            try:
                costo = float(input("Costo produzione: "))
                prezzo = float(input("Prezzo vendita: "))
<<<<<<< HEAD
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
=======
                quantita = int(input("Quantità da aggiungere: "))
                if quantita <= 0 or costo < 0 or prezzo < 0:
                    raise ValueError
            except ValueError:
                print(" Inserisci valori numerici validi e positivi.")
                continue

            if tipo == "elettronica":
                garanzia = input("Garanzia (anni): ")
                prodotto = Elettronica(nome, costo, prezzo, garanzia)
            elif tipo == "abbigliamento":
                materiale = input("Materiale: ")
                prodotto = Abbigliamento(nome, costo, prezzo, materiale)
            else:
                print(" Tipo non riconosciuto.")
>>>>>>> bba2dae5e5d0ec98b40464dc41b3c057c379535b
                continue

            fabbrica.aggiungi_prodotto(prodotto, quantita)

        elif scelta == "2":
            nome = input("Nome prodotto da vendere: ").strip()
            try:
<<<<<<< HEAD
                quantita = int(input("Quantità: "))
                if quantita <= 0:
                    raise ValueError
            except ValueError:
                print("Quantità non valida.")
=======
                quantita = int(input("Quantità da vendere: "))
                if quantita <= 0:
                    raise ValueError
            except ValueError:
                print(" Inserisci una quantità valida.")
>>>>>>> bba2dae5e5d0ec98b40464dc41b3c057c379535b
                continue

            fabbrica.vendi_prodotto(nome, quantita)

        elif scelta == "3":
<<<<<<< HEAD
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

=======
            fabbrica.stampa_inventario()

        elif scelta == "4":
            nome = input("Nome prodotto restituito: ").strip()
            try:
                quantita = int(input("Quantità da restituire: "))
                if quantita <= 0:
                    raise ValueError
            except ValueError:
                print(" Inserisci una quantità valida.")
                continue

            fabbrica.resi_prodotto(nome, quantita)

        elif scelta == "5":
            print(f"\nBudget attuale: {fabbrica.budget:.2f} €")
            print(f"Profitto totale: {fabbrica.profitto_totale:.2f} €")

        elif scelta == "0":
            print("Uscita dal programma.")
            break
>>>>>>> bba2dae5e5d0ec98b40464dc41b3c057c379535b
        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    menu_fabbrica()
