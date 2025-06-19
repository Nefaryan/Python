# ==========================================================
# 1. Classe OggettoMagico
#    – singola “scheda” di un prodotto magico
# ==========================================================

class OggettoMagico:
    def __init__(self, nome: str, potere: str, prezzo: float, quantita: int):
        self.nome = nome
        self.potere = potere
        self.prezzo = prezzo
        self.quantita = quantita

    def descrizione(self) -> None:
        """Stampa tutte le informazioni dell’oggetto in modo leggibile."""
        print(f"• {self.nome} | Potere: {self.potere} | "
              f"Prezzo: {self.prezzo:.2f}Ore | Disponibili: {self.quantita}")


# ==========================================================
# 2. “Contenitori” Pozione / Artefatto / Pergamena
#    – nessuna ereditarietà, contengono solo un OggettoMagico
# ==========================================================

class Pozione:
    def __init__(self, oggetto: OggettoMagico):
        self.oggetto = oggetto


class Artefatto:
    def __init__(self, oggetto: OggettoMagico):
        self.oggetto = oggetto


class Pergamena:
    def __init__(self, oggetto: OggettoMagico):
        self.oggetto = oggetto


# ==========================================================
# 3. Classe BottegaMagica
#    – gestisce oro e inventario diviso in categorie
# ==========================================================

class BottegaMagica:
    def __init__(self, oro_iniziale: float = 100.0):
        self.oro = oro_iniziale
        # inventario = {"Pozioni": [Pozione, ...], "Artefatti": [...], "Pergamene":[...]}
        self.inventario: dict[str, list] = {
            "Pozioni": [],
            "Artefatti": [],
            "Pergamene": []
        }

    # ------------------------ metodi pubblici ------------------------

    def reso(self, nome_oggetto: str, categoria: str, quantita: int):
        if quantita <= 0:
            print("Quantità non valida.")
            return

        categoria = categoria.lower()

        # Determina classe contenitore e chiave inventario manualmente
        if categoria in ["pozione", "pozioni"]:
            cls_cont = Pozione
            cat_key = "Pozioni"
        elif categoria in ["artefatto", "artefatti"]:
            cls_cont = Artefatto
            cat_key = "Artefatti"
        elif categoria in ["pergamena", "pergamene"]:
            cls_cont = Pergamena
            cat_key = "Pergamene"
        else:
            print("Categoria non valida.")
            return

        # Cerca l’oggetto nella categoria corretta
        cont = self.cerca_oggetto(nome_oggetto, cat_key)

        if not cont:
            print("L’oggetto era assente, lo reinserisco in inventario.")
            print("   (serve dettaglio potere e prezzo per ricrearlo)")
            potere = input("   Descrivi il potere: ")
            try:
                prezzo = float(input("   Prezzo di vendita (Oro): "))
            except ValueError:
                print("   Prezzo non valido, annullo reso.")
                return
            ogg = OggettoMagico(nome_oggetto, potere, prezzo, quantita)
            cont = cls_cont(ogg)
            self.inventario[cat_key].append(cont)
        else:
            cont.oggetto.quantita += quantita

        rimborso = cont.oggetto.prezzo * quantita
        if rimborso > self.oro:
            print("Oro insufficiente in cassa per il rimborso.")
            cont.oggetto.quantita -= quantita  # rollback
            return

        self.oro -= rimborso
        print(f" Reso di {quantita}× '{cont.oggetto.nome}'. Rimborsati {rimborso:.2f} Oro.")

     

    def aggiungi(self, categoria: str, oggetto_contenitore):

        cat = categoria.capitalize()
        if cat not in self.inventario:
            print("Categoria non valida.")
            return
        self.inventario[cat].append(oggetto_contenitore)
        print(f"Aggiunto '{oggetto_contenitore.oggetto.nome}' alla sezione {cat}.")

    def mostra_inventario(self):

        print("\nINVENTARIO BOTTEGA")
        for cat, lista in self.inventario.items():
            print(f"\n{cat.upper()}")
            if not lista:
                print("  (vuoto)")
            else:
                for cont in lista:
                    cont.oggetto.descrizione()
        print(f"\n Oro in cassa: {self.oro:.2f}Oro\n")

    def cerca_oggetto(self, nome_oggetto: str, categoria: str):

        cat = categoria.capitalize()
        if cat not in self.inventario:
            return None
        for cont in self.inventario[cat]:
            if cont.oggetto.nome.lower() == nome_oggetto.lower():
                return cont
        return None

    def vendi(self, nome_oggetto: str, categoria: str, quantita: int):

        cont = self.cerca_oggetto(nome_oggetto, categoria)
        if not cont:
            print("oggetto non trovato.")
            return
        if quantita <= 0:
            print(" Quantità non valida.")
            return
        if cont.oggetto.quantita < quantita:
            print("Quantità richiesta superiore allo stock.")
            return

        cont.oggetto.quantita -= quantita
        ricavo = cont.oggetto.prezzo * quantita
        self.oro += ricavo
        print(f"Vendute {quantita}x '{cont.oggetto.nome}' per {ricavo:.2f} oro.")

        # se esaurito, rimuovilo dalla lista di categoria
        if cont.oggetto.quantita == 0:
            self.inventario[categoria.capitalize()].remove(cont)
            print(f" '{cont.oggetto.nome}' esaurito ed eliminato dall’inventario.")




def menu():
    shop = BottegaMagica(oro_iniziale=245423100.0)

    while True:
        print("\n MENU BOTTEGA MAGICA ")
        print("1. Aggiungi oggetto")
        print("2. Mostra inventario")
        print("3. Vendi oggetto")
        print("4. Reso oggetto")
        print("5. Cerca oggetto")
        print("0. Esci")
        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            categoria = input("Categoria (Pozioni / Artefatti / Pergamene): ").capitalize()
            if categoria not in ["Pozioni", "Artefatti", "Pergamene"]:
                print(" Categoria non valida.")
                continue

            nome = input("Nome dell’oggetto: ")
            potere = input("Descrizione del potere: ")
            try:
                prezzo = float(input("Prezzo di vendita (Oro): "))
                quantita = int(input("Quantità disponibile: "))
            except ValueError:
                print("Prezzo o quantità non validi.")
                continue

            oggetto = OggettoMagico(nome, potere, prezzo, quantita)
            contenitore = {"Pozioni": Pozione, "Artefatti": Artefatto, "Pergamene": Pergamena}[categoria](oggetto)
            shop.aggiungi(categoria, contenitore)

        elif scelta == "2":
            shop.mostra_inventario()

        elif scelta == "3":
            categoria = input("Categoria: ").capitalize()
            nome = input("Nome dell’oggetto da vendere: ")
            try:
                quantita = int(input("Quantità da vendere: "))
            except ValueError:
                print("Quantità non valida.")
                continue
            shop.vendi(nome, categoria, quantita)

        elif scelta == "4":
            categoria = input("Categoria: ").capitalize()
            nome = input("Nome dell’oggetto da restituire: ")
            try:
                quantita = int(input("Quantità da restituire: "))
            except ValueError:
                print("Quantità non valida.")
                continue
            shop.reso(nome, categoria, quantita)

        elif scelta == "5":
            categoria = input("Categoria: ").capitalize()
            nome = input("Nome dell’oggetto da cercare: ")
            ogg = shop.cerca_oggetto(nome, categoria)
            if ogg:
                print(" Oggetto trovato:")
                ogg.oggetto.descrizione()
            else:
                print(" Oggetto non trovato.")

        elif scelta == "0":
            print(" Uscita dal programma. A presto, mago!")
            break

        else:
            print(" Scelta non valida.")


# Avvio interattivo
if __name__ == "__main__":
    menu()


