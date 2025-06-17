import time

class Ristorante:
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False
        self.menu = {}

    def descrivi_ristorante(self):
        print(f"\nIl ristorante '{self.nome}' offre cucina {self.tipo_cucina}.")

    def stato_apertura(self):
        print(f"Stato: {'APERTO' if self.aperto else 'CHIUSO'}")

    def apri_ristorante(self):
        self.aperto = True
        print("Il ristorante è ora aperto.")

    def chiudi_ristorante(self):
        self.aperto = False
        print("Il ristorante è ora chiuso.")

    def aggiungi_al_menu(self, piatto, prezzo):
        if piatto in self.menu:
            print(f" Il piatto '{piatto}' è già nel menu.")
        else:
            self.menu[piatto] = prezzo
            print(f"'{piatto}' aggiunto al menu a €{prezzo:.2f}.")

    def togli_dal_menu(self, piatto):
        if piatto in self.menu:
            del self.menu[piatto]
            print(f"'{piatto}' rimosso dal menu.")
        else:
            print(f"Il piatto '{piatto}' non è nel menu.")

    def stampa_menu(self):
        if not self.menu:
            print("Il menu è vuoto.")
        else:
            print("Menu attuale:")
            for piatto, prezzo in self.menu.items():
                print(f"- {piatto}: €{prezzo:.2f}")


nome = input("Inserisci il nome del ristorante: ")
tipo = input("Inserisci il tipo di cucina offerta: ")
ristorante = Ristorante(nome, tipo)

while True:
    print("\n--- Menu Gestione Ristorante ---")
    print("1. Descrivi ristorante")
    print("2. Stato apertura")
    print("3. Apri ristorante")
    print("4. Chiudi ristorante")
    print("5. Aggiungi piatto al menu")
    print("6. Rimuovi piatto dal menu")
    print("7. Stampa menu")
    print("0. Esci")

    scelta = input("Seleziona un'opzione: ")

    if scelta == "1":
        ristorante.descrivi_ristorante()
    elif scelta == "2":
        ristorante.stato_apertura()
    elif scelta == "3":
        ristorante.apri_ristorante()
    elif scelta == "4":
        ristorante.chiudi_ristorante()
    elif scelta == "5":
        piatto = input("Nome del piatto da aggiungere: ")
        try:
            prezzo = float(input("Prezzo del piatto: "))
            ristorante.aggiungi_al_menu(piatto, prezzo)
        except ValueError:
            print("Prezzo non valido.")
    elif scelta == "6":
        piatto = input("Nome del piatto da rimuovere: ")
        ristorante.togli_dal_menu(piatto)
    elif scelta == "7":
        ristorante.stampa_menu()
    elif scelta == "0":
        print("Uscita dal programma. Arrivederci!")
        break
    else:
        print("Scelta non valida. Riprova.")
    time.sleep(3)
